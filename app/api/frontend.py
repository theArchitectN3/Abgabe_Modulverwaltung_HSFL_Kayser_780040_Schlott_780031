from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.application.service import ModulWorkflowService
from app.domain import schemas
from typing import Optional

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def dashboard(
    request: Request, 
    role: str = "lecturer", 
    user_id: Optional[int] = None,
    time_range: str = "all", # NEU: Zeitfilter
    db: Session = Depends(get_db)
):
    role = role.strip().lower()
    service = ModulWorkflowService(db)
    
    users_data = service.get_users_for_selection()
    
    context_data = {
        "request": request,
        "current_role": role,
        "selected_user_id": user_id,
        "selected_time_range": time_range, # An Template weitergeben
        "all_students": users_data["students"],
        "all_lecturers": users_data["lecturers"]
    }

    if role == "student":
        if user_id:
            data = service.get_student_dashboard(user_id)
            if data: context_data.update(data)

    elif role == "lecturer":
        if user_id:
            data = service.get_lecturer_dashboard(user_id)
            if data: context_data.update(data)

    elif role in ["coordinator", "commission", "dean"]:
        # Zeitfilter an Service uebergeben
        data = service.get_reviewer_dashboard(role, time_range)
        context_data.update(data)

    return templates.TemplateResponse("index.html", context_data)

# --- ACTIONS & DETAILS ---

@router.get("/module/{module_id}", response_class=HTMLResponse)
def detail_module(
    module_id: int, 
    request: Request, 
    role: str = "lecturer", 
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    service = ModulWorkflowService(db)
    modul = service.get_module(module_id)
    return templates.TemplateResponse("detail.html", {
        "request": request, 
        "modul": modul,
        "current_role": role,
        "user_id": user_id 
    })

@router.get("/create", response_class=HTMLResponse)
def show_create_form(request: Request, role: str = "lecturer", user_id: Optional[int] = None):
    return templates.TemplateResponse("create.html", {"request": request, "current_role": role, "user_id": user_id})

@router.post("/create")
def handle_create_form(
    code: str = Form(...),
    title: str = Form(...),
    ects: int = Form(...),
    description: str = Form(...),
    semester: int = Form(1), 
    role: str = Form("lecturer"),
    user_id: int = Form(...), 
    db: Session = Depends(get_db)
):
    service = ModulWorkflowService(db)
    dto = schemas.ModuleCreate(
        code=code, title=title, ects=ects, description=description, 
        semester=semester, lecturer_id=user_id
    )
    try:
        service.create_module(dto)
        return RedirectResponse(url=f"/?role={role}&user_id={user_id}", status_code=303)
    except Exception as e:
        return f"Error: {e}"

@router.get("/module/{module_id}/edit", response_class=HTMLResponse)
def show_edit_form(
    module_id: int, 
    request: Request, 
    role: str = "lecturer", 
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    service = ModulWorkflowService(db)
    modul = service.get_module(module_id)
    return templates.TemplateResponse("edit.html", {
        "request": request, 
        "modul": modul, 
        "current_role": role,
        "user_id": user_id
    })

@router.post("/module/{module_id}/edit")
def handle_edit_form(
    module_id: int,
    title: str = Form(...),
    ects: int = Form(...),
    description: str = Form(...),
    role: str = Form("lecturer"),
    user_id: Optional[int] = Form(None),
    db: Session = Depends(get_db)
):
    service = ModulWorkflowService(db)
    dto = schemas.ModuleUpdate(title=title, ects=ects, description=description)
    try:
        service.update_module(module_id, dto)
        url = f"/module/{module_id}?role={role}"
        if user_id: url += f"&user_id={user_id}"
        return RedirectResponse(url=url, status_code=303)
    except Exception as e:
         return f"Error: {e}"

@router.post("/module/{module_id}/delete")
def handle_delete(module_id: int, role: str = Form("lecturer"), user_id: Optional[int] = Form(None), db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    service.delete_module(module_id)
    url = f"/?role={role}"
    if user_id: url += f"&user_id={user_id}"
    return RedirectResponse(url=url, status_code=303)

@router.get("/admin", response_class=HTMLResponse)
def admin_panel(request: Request, role: str = "dean", db: Session = Depends(get_db)):
    if role != "dean": return RedirectResponse(url=f"/?role={role}") 
    service = ModulWorkflowService(db)
    return templates.TemplateResponse("admin.html", {
        "request": request, 
        "current_role": role,
        "users": service.get_all_users(),
        "programs": service.get_all_programs()
    })

@router.post("/admin/users")
def create_user(
    username: str = Form(...), full_name: str = Form(...), role_type: str = Form(...),
    current_role: str = Form(...), db: Session = Depends(get_db)
):
    service = ModulWorkflowService(db)
    dto = schemas.UserCreate(username=username, full_name=full_name, role=role_type)
    service.create_user(dto)
    return RedirectResponse(url=f"/admin?role={current_role}", status_code=303)

@router.post("/admin/programs")
def create_program(name: str = Form(...), current_role: str = Form(...), db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    dto = schemas.ProgramCreate(name=name)
    service.create_program(dto)
    return RedirectResponse(url=f"/admin?role={current_role}", status_code=303)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.application.service import ModulWorkflowService
from app.domain import schemas

router = APIRouter()

# --- Module Management ---

@router.post("/modules", response_model=schemas.ModuleResponse, tags=["Modules"])
def create_module(module: schemas.ModuleCreate, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.create_module(module)

@router.get("/modules/{module_id}", response_model=schemas.ModuleResponse, tags=["Modules"])
def get_module(module_id: int, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    modul = service.get_module(module_id)
    if not modul:
        raise HTTPException(status_code=404, detail="Module not found")
    return modul

@router.put("/modules/{module_id}", response_model=schemas.ModuleResponse, tags=["Modules"])
def update_module(module_id: int, update: schemas.ModuleUpdate, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.update_module(module_id, update)

@router.delete("/modules/{module_id}", tags=["Modules"])
def delete_module(module_id: int, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.delete_module(module_id)

# --- User Management ---

@router.post("/users", response_model=schemas.UserResponse, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.create_user(user)

@router.get("/users", response_model=List[schemas.UserResponse], tags=["Users"])
def list_users(db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.get_all_users()

@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.delete_user(user_id)

# --- Study Programs & ECTS ---

@router.post("/programs", response_model=schemas.ProgramResponse, tags=["Study Programs"])
def create_program(prog: schemas.ProgramCreate, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.create_program(prog)

@router.get("/programs", response_model=List[schemas.ProgramResponse], tags=["Study Programs"])
def list_programs(db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.get_all_programs()

@router.get("/programs/{program_id}/ects", tags=["Study Programs"])
def calculate_ects(program_id: int, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.calculate_program_ects(program_id)

# --- Workflow ---

@router.post("/modules/{module_id}/submit", response_model=schemas.ModuleResponse, tags=["Workflow"])
def submit_module(module_id: int, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.submit_module(module_id)

@router.post("/modules/{module_id}/approve", response_model=schemas.ModuleResponse, tags=["Workflow"])
def approve_module(module_id: int, decision: schemas.Decision, db: Session = Depends(get_db)):
    service = ModulWorkflowService(db)
    return service.approve_module(module_id, decision.comment)

@router.post("/modules/{module_id}/reject", response_model=schemas.ModuleResponse, tags=["Workflow"])
def reject_module(module_id: int, decision: schemas.Decision, db: Session = Depends(get_db)):
    if not decision.comment:
        raise HTTPException(status_code=400, detail="Comment required for rejection.")
    service = ModulWorkflowService(db)
    return service.reject_module(module_id, decision.comment)
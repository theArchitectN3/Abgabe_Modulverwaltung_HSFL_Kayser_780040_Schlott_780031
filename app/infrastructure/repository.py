from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.domain import models, schemas
from sqlalchemy import desc

class ModulRepository:
    """
    Infrastructure Layer: Handles direct database interactions.
    """
    def __init__(self, db: Session):
        self.db = db

    # --- Generics ---
    def delete(self, model_obj):
        self.db.delete(model_obj)
        self.db.commit()

    # --- Module Methods ---
    def get_module_by_id(self, module_id: int) -> models.Module:
        return self.db.query(models.Module).options(joinedload(models.Module.history)).filter(models.Module.id == module_id).first()

    def get_all_modules(self):
        return self.db.query(models.Module).options(joinedload(models.Module.lecturer)).all()

    def get_modules_by_lecturer(self, lecturer_id: int):
        return self.db.query(models.Module).filter(models.Module.lecturer_id == lecturer_id).all()

    def get_modules_by_status(self, status_list: list):
        return self.db.query(models.Module).options(joinedload(models.Module.lecturer)).filter(models.Module.status.in_(status_list)).all()

    def get_modules_by_program(self, program_id: int):
        return self.db.query(models.Module).join(models.StudyRegulation).filter(models.StudyRegulation.program_id == program_id).all()

    def create_module(self, module_data: schemas.ModuleCreate) -> models.Module:
        try:
            db_module = models.Module(**module_data.model_dump(), status="DRAFT")
            self.db.add(db_module)
            self.db.commit()
            self.db.refresh(db_module)
            return db_module
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Module code already exists.")

    def update_module_content(self, module: models.Module, data: schemas.ModuleUpdate):
        if data.title: module.title = data.title
        if data.ects: module.ects = data.ects
        if data.description: module.description = data.description
        self.db.commit()
        self.db.refresh(module)
        return module

    def update_status(self, module_id: int, new_status: str) -> models.Module:
        module = self.get_module_by_id(module_id)
        if module:
            module.status = new_status
            self.db.commit()
            self.db.refresh(module)
        return module

    # --- History / Analytics ---
    def add_history_entry(self, entry: models.HistoryEntry):
        self.db.add(entry)
        self.db.commit()

    def get_history_by_role(self, role_name: str, limit: int = 5):
        """Fetches the last N decisions made by a specific role."""
        return self.db.query(models.HistoryEntry)\
            .filter(models.HistoryEntry.reviewer_role == role_name)\
            .order_by(desc(models.HistoryEntry.id))\
            .limit(limit).all()

    # --- User Methods ---
    def create_user(self, user: schemas.UserCreate):
        try:
            db_user = models.User(**user.model_dump())
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Username already exists.")

    def get_user(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()
    
    def get_all_users(self):
        return self.db.query(models.User).all()

    def get_users_by_role(self, role: str):
        return self.db.query(models.User).filter(models.User.role == role).all()

    # --- Program Methods ---
    def create_program(self, program: schemas.ProgramCreate):
        db_prog = models.StudyProgram(**program.model_dump())
        self.db.add(db_prog)
        self.db.commit()
        self.db.refresh(db_prog)
        return db_prog

    def get_program(self, prog_id: int):
        return self.db.query(models.StudyProgram).filter(models.StudyProgram.id == prog_id).first()

    def get_all_programs(self):
        return self.db.query(models.StudyProgram).all()
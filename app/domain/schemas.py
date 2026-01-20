from pydantic import BaseModel
from typing import Optional

# --- Module Schemas ---
class ModuleCreate(BaseModel):
    title: str
    code: str
    ects: int
    semester: int = 1
    description: Optional[str] = None
    regulation_id: Optional[int] = None
    lecturer_id: Optional[int] = None

class ModuleUpdate(BaseModel):
    title: Optional[str] = None
    ects: Optional[int] = None
    description: Optional[str] = None
    semester: Optional[int] = None

class ModuleResponse(ModuleCreate):
    id: int
    status: str
    lecturer_id: Optional[int] = None
    class Config:
        from_attributes = True

# --- User Schemas ---
class UserCreate(BaseModel):
    username: str
    full_name: str
    role: str 
    study_program_id: Optional[int] = None

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True

# --- Program Schemas ---
class ProgramCreate(BaseModel):
    name: str

class ProgramResponse(ProgramCreate):
    id: int
    class Config:
        from_attributes = True

# --- Workflow Schemas ---
class Decision(BaseModel):
    comment: Optional[str] = None
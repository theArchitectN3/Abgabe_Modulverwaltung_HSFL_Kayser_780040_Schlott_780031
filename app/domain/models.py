from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    role = Column(String) 
    
    current_semester = Column(Integer, default=1)

    study_program_id = Column(Integer, ForeignKey("study_programs.id"), nullable=True)
    study_program = relationship("StudyProgram")

class StudyProgram(Base):
    __tablename__ = "study_programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    regulations = relationship("StudyRegulation", back_populates="program")

class StudyRegulation(Base):
    __tablename__ = "study_regulations"
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String)
    valid_from = Column(String)
    
    program_id = Column(Integer, ForeignKey("study_programs.id"))
    program = relationship("StudyProgram", back_populates="regulations")
    
    modules = relationship("Module", back_populates="regulation")

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    code = Column(String, unique=True, index=True)
    description = Column(Text)
    ects = Column(Integer)

    semester = Column(Integer, default=1) 
    status = Column(String, default="DRAFT") 
    
    regulation_id = Column(Integer, ForeignKey("study_regulations.id"), nullable=True)
    regulation = relationship("StudyRegulation", back_populates="modules")
    
    lecturer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    lecturer = relationship("User", foreign_keys=[lecturer_id])

    history = relationship("HistoryEntry", back_populates="module", cascade="all, delete-orphan")

class HistoryEntry(Base):
    __tablename__ = "history_entries"
    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"))
    timestamp = Column(String)
    comment = Column(Text)
    decision = Column(Boolean)
    reviewer_role = Column(String)
    
    module = relationship("Module", back_populates="history")
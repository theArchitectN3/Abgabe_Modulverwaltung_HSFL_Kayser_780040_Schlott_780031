from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.infrastructure.repository import ModulRepository
from app.domain import models, schemas
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import random

class ModulWorkflowService:
    def __init__(self, db: Session):
        self.repository = ModulRepository(db)

    def get_users_for_selection(self):
        return {
            "students": self.repository.get_users_by_role("Student"),
            "lecturers": self.repository.get_users_by_role("Lecturer")
        }

    def get_student_dashboard(self, student_id: int):
        student = self.repository.get_user(student_id)
        if not student or not student.study_program_id:
            return None
        program = self.repository.get_program(student.study_program_id)
        all_modules = self.repository.get_modules_by_program(program.id)
        
        visible_modules = [m for m in all_modules if m.status == "RELEASED"]
        
        # --- DYNAMIC SEMESTER COUNT ---
        # Determine max semester based on program name/content
        max_semesters = 6 # Default
        if "Seeverkehr" in program.name: max_semesters = 8
        elif "Biotechnologie" in program.name: max_semesters = 7
        
        # Initialize layout
        modules_by_semester = {i: [] for i in range(1, max_semesters + 1)}
        
        total_ects = 0
        current_semester_num = student.current_semester if student.current_semester else 1
        current_semester_load = 0 
        achieved_ects = 0         
        
        student_grades = {}
        semester_averages = {}
        possible_grades = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
        overall_grade_sum = 0
        graded_count = 0

        for m in visible_modules:
            if m.semester in modules_by_semester:
                modules_by_semester[m.semester].append(m)
            else:
                modules_by_semester.setdefault(m.semester, []).append(m)
            
            total_ects += m.ects
            
            if m.semester < current_semester_num:
                achieved_ects += m.ects
                random.seed(student.id + m.id)
                g = random.choice(possible_grades)
                student_grades[m.id] = g
                
                if m.semester not in semester_averages: semester_averages[m.semester] = []
                semester_averages[m.semester].append(g)
                
                overall_grade_sum += g
                graded_count += 1
            elif m.semester == current_semester_num:
                current_semester_load += m.ects
                student_grades[m.id] = "In Progress"
            else:
                student_grades[m.id] = "-"

        chart_labels = []
        chart_values = []
        
        for sem, grades in sorted(semester_averages.items()):
            avg = sum(grades) / len(grades)
            chart_labels.append(f"Sem {sem}")
            chart_values.append(round(avg, 2))
            
        overall_average = round(overall_grade_sum / graded_count, 2) if graded_count > 0 else 0.0

        return {
            "student": student, 
            "program": program,
            "modules_by_semester": modules_by_semester, 
            "total_ects": total_ects,
            "current_semester_load": current_semester_load,
            "achieved_ects": achieved_ects,
            "grades": student_grades,
            "overall_average": overall_average,
            "chart_labels": chart_labels,
            "chart_values": chart_values
        }
    
    def get_lecturer_dashboard(self, lecturer_id: int):
        modules = self.repository.get_modules_by_lecturer(lecturer_id)
        return {
            "drafts": [m for m in modules if m.status in ["DRAFT", "CHANGES_REQUIRED"]],
            "in_review": [m for m in modules if "REVIEW" in m.status],
            "published": [m for m in modules if m.status == "RELEASED"]
        }

    def get_reviewer_dashboard(self, role: str, time_range: str = "all"):
        target_status = ""
        role_db_name = "" 
        if role == "coordinator": 
            target_status = "REVIEW_COORDINATOR"
            role_db_name = "Program Coordinator"
        elif role == "commission": 
            target_status = "REVIEW_COMMISSION"
            role_db_name = "Study Commission"
        elif role == "dean": 
            target_status = "REVIEW_DEAN"
            role_db_name = "Dean"
        
        todo_list = self.repository.get_modules_by_status([target_status])
        data = {"todo_list": todo_list}

        cutoff_date = None
        now = datetime.now()
        if time_range == "1M": cutoff_date = now - timedelta(days=30)
        elif time_range == "3M": cutoff_date = now - timedelta(days=90)
        elif time_range == "6M": cutoff_date = now - timedelta(days=180)
        elif time_range == "1Y": cutoff_date = now - timedelta(days=365)
        
        def is_recent(date_str):
            if not cutoff_date: return True
            try: return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") >= cutoff_date
            except: return False

        if role == "coordinator":
            all_mods = self.repository.get_all_modules()
            filtered_mods = []
            for m in all_mods:
                if cutoff_date and m.history:
                    if is_recent(m.history[-1].timestamp): filtered_mods.append(m)
                else: filtered_mods.append(m)

            status_counts = Counter([m.status for m in filtered_mods])
            formatted_labels = [k.replace('_', ' ').title() for k in status_counts.keys()]
            data["all_modules"] = all_mods 
            data["chart_labels"] = formatted_labels
            data["chart_values"] = list(status_counts.values())
        
        elif role == "commission":
            all_hist = self.repository.get_history_by_role(role_db_name, limit=100)
            filtered_hist = [h for h in all_hist if is_recent(h.timestamp)]
            approvals = sum(1 for h in filtered_hist if h.decision)
            rejections = sum(1 for h in filtered_hist if not h.decision)
            data["recent_history"] = filtered_hist[:10]
            data["chart_data"] = [approvals, rejections]
            
        elif role == "dean":
            all_mods = self.repository.get_all_modules()
            filtered_mods = []
            for m in all_mods:
                if cutoff_date and m.history:
                     if is_recent(m.history[-1].timestamp): filtered_mods.append(m)
                else: filtered_mods.append(m)
            status_counts = Counter([m.status for m in filtered_mods])
            formatted_labels = [k.replace('_', ' ').title() for k in status_counts.keys()]
            data["all_modules"] = all_mods
            data["chart_labels"] = formatted_labels
            data["chart_values"] = list(status_counts.values())

        return data

    def create_module(self, data: schemas.ModuleCreate): return self.repository.create_module(data)
    def get_module(self, module_id: int): return self.repository.get_module_by_id(module_id)
    def update_module(self, module_id: int, data: schemas.ModuleUpdate):
        module = self.repository.get_module_by_id(module_id)
        if not module: raise HTTPException(status_code=404, detail="Module not found")
        if module.status == "RELEASED": raise HTTPException(status_code=400, detail="Cannot edit released modules.")
        return self.repository.update_module_content(module, data)
    def delete_module(self, module_id: int):
        module = self.repository.get_module_by_id(module_id)
        if not module: raise HTTPException(status_code=404, detail="Module not found")
        self.repository.delete(module)
        return {"status": "deleted", "id": module_id}
    def create_user(self, data: schemas.UserCreate): return self.repository.create_user(data)
    def get_all_users(self): return self.repository.get_all_users()
    def get_user(self, user_id: int): return self.repository.get_user(user_id)
    def delete_user(self, user_id: int):
        user = self.repository.get_user(user_id)
        if not user: raise HTTPException(status_code=404, detail="User not found")
        self.repository.delete(user)
        return {"status": "deleted"}
    def create_program(self, data: schemas.ProgramCreate): return self.repository.create_program(data)
    def get_all_programs(self): return self.repository.get_all_programs()
    def calculate_program_ects(self, program_id: int):
        program = self.repository.get_program(program_id)
        if not program: raise HTTPException(status_code=404, detail="Program not found")
        total_ects = sum(m.ects for r in program.regulations for m in r.modules if m.status == "RELEASED")
        return {"program": program.name, "total_ects": total_ects}
    def submit_module(self, module_id: int):
        module = self.repository.get_module_by_id(module_id)
        if not module or module.status not in ["DRAFT", "CHANGES_REQUIRED"]: raise HTTPException(status_code=400, detail="Error")
        if not (module.title and module.ects and module.ects > 0 and module.description): raise HTTPException(status_code=400, detail="Missing fields")
        return self._change_status(module, "REVIEW_COORDINATOR", "Author", "Submitted for review")
    def approve_module(self, module_id: int, comment: str = None):
        module = self.repository.get_module_by_id(module_id)
        current = module.status
        if current == "REVIEW_COORDINATOR": next_s, role = "REVIEW_COMMISSION", "Program Coordinator"
        elif current == "REVIEW_COMMISSION": next_s, role = "REVIEW_DEAN", "Study Commission"
        elif current == "REVIEW_DEAN": next_s, role = "RELEASED", "Dean"
        else: raise HTTPException(status_code=400, detail="Error")
        return self._change_status(module, next_s, role, comment or "Approved", True)
    def reject_module(self, module_id: int, comment: str):
        module = self.repository.get_module_by_id(module_id)
        if module.status in ["DRAFT", "RELEASED"]: raise HTTPException(status_code=400, detail="Error")
        return self._change_status(module, "CHANGES_REQUIRED", "Reviewer", comment, False)
    def _change_status(self, module, new_status, role, comment, decision=True):
        self.repository.update_status(module.id, new_status)
        self.repository.add_history_entry(models.HistoryEntry(
            module_id=module.id, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            comment=comment, decision=decision, reviewer_role=role
        ))
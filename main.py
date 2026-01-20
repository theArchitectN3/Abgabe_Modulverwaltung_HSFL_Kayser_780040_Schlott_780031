import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import controller
from app.api import frontend
from app.database import engine
from app.domain import models
from init_db import create_data

# --- LIFESPAN MANAGER ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("-----------------------------------------------------")
    print("🚀 SYSTEM STARTUP: Initializing Database & Mock Data...")
    
    models.Base.metadata.create_all(bind=engine)
    
    try:
        create_data()
        print("✅ DATABASE: Populated successfully with 70 students & staff.")
    except Exception as e:
        print(f"⚠️ WARNING: Database initialization failed: {e}")
        
    print("-----------------------------------------------------")
    yield
    print("🛑 SYSTEM SHUTDOWN")

# --- APP DEFINITION ---
app = FastAPI(
    title="Modulverwaltung HS Flensburg",
    description="Backend für die Modulverwaltung basierend auf Clean Architecture.",
    version="1.0.0",
    lifespan=lifespan
)

# API Router (JSON)
app.include_router(controller.router)

# Frontend Router (HTML)
app.include_router(frontend.router)

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:8080")
    
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
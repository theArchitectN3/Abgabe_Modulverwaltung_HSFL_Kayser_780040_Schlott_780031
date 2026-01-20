from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Pfad zur SQLite-Datenbankdatei
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Engine erstellen: check_same_thread=False ist für SQLite notwendig
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session-Fabrik für Datenbankverbindungen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisklasse für ORM-Modelle
Base = declarative_base()

def get_db():
    """Dependency Injection Funktion für FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Function to initialize DB
def init_db():
    from backend.db.models import Base
    print("Starting schema creation...")
    Base.metadata.create_all(bind=engine)
    print("Schema creation completed.")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

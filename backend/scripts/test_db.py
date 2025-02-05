from sqlalchemy.sql import text
from backend.db.database import SessionLocal, init_db  # Import init_db to initialize the schema
from backend.db.models import Base


def test_connection():
    try:
        # Initialize the database schema
        print("Initializing the database...")
        init_db()
        print("Database schema initialized successfully.")

        # Test session-based connection
        db = SessionLocal()
        result = db.execute(text("SELECT 1")).fetchall()
        print("Session-based connection successful:", result)
        db.close()

    except Exception as e:
        print("Database connection failed:", str(e))

if __name__ == "__main__":
    test_connection()

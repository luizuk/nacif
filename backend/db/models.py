from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Avoid importing Base directly from database.py to resolve circular imports
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    username = Column(String, unique=True, nullable=False, index=True)  # Unique username
    password = Column(String, nullable=False)  # Password for the user

    # One-to-Many relationship: A user can have many todos
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")


# Todo Model
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    title = Column(String, nullable=False)  # Title of the task
    description = Column(String)  # Optional description
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to User table

    # Many-to-One relationship: A todo belongs to one user
    owner = relationship("User", back_populates="todos")

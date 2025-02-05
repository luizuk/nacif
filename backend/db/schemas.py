from pydantic import BaseModel
from typing import List, Optional


# Base schema for creating a new user
class UserBase(BaseModel):
    username: str


# Schema for creating a user (input from the client)
class UserCreate(UserBase):
    password: str


# Schema for returning user details (response to the client)
class UserResponse(UserBase):
    id: int
    todos: List["TodoResponse"] = []  # Includes associated todos

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy objects to Pydantic models


# Base schema for creating a new todo
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


# Schema for creating a todo (input from the client)
class TodoCreate(TodoBase):
    pass


# Schema for returning todo details (response to the client)
class TodoResponse(TodoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Required to resolve circular references in Pydantic
UserResponse.update_forward_refs()

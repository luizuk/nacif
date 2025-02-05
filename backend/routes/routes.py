from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import models, database, schemas
from backend.auth.auth import verify_password, create_access_token, verify_token,oauth2_scheme
from backend.db.database import get_db

router = APIRouter()

@router.post("/token")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Fetch the user from the database
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create an access token
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Example implementation for login
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user:
        return {"error": "User not found"}
    return {"message": "Login successful"}

@router.get("/protected-endpoint")
def protected_route(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    return {"message": f"Welcome, {user}"}


# Create a new Todo item
@router.post("/todos/", response_model=schemas.TodoResponse)
def create_todo(
    todo: schemas.TodoCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Verify the user from the token
    username = verify_token(token)
    
    # Check if the user exists
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Create a new Todo item
    new_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        user_id=db_user.id,  # Link todo to the user
    )
    
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    
    return new_todo


@router.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(
    todo_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Verify the user from the token
    username = verify_token(token)

    # Check if the user exists
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Fetch the todo item
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == db_user.id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )

    return todo


@router.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(
    todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Verify the user from the token
    username = verify_token(token)

    # Check if the user exists
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Fetch the todo item
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == db_user.id).first()
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )

    # Update the todo item
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)

    return db_todo


@router.delete("/todos/{todo_id}", response_model=schemas.TodoResponse)
def delete_todo(
    todo_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    # Verify the user from the token
    username = verify_token(token)

    # Check if the user exists
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Fetch the todo item
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == db_user.id).first()
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )

    # Delete the todo item
    db.delete(db_todo)
    db.commit()

    return db_todo

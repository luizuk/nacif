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

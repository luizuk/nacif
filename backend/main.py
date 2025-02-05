from fastapi import FastAPI
from backend.db.database import init_db
from backend.routes import router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}

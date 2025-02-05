from fastapi import FastAPI
from backend.db.database import init_db
from backend.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}

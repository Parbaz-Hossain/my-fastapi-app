from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import app.scm_module.production.models as models

models.Base.metadata.create_all(bind=engine)

# Import routers from the SCM module
from app.scm_module.routes import router as scm_router

# Import routers from the User module


app = FastAPI(
    title="My FastAPI App",
    description="A beginner-friendly API for learning FastAPI in Python!",
    version="1.1.0",
    openapi_tags=[
        {"name": "General", "description": "General or health check endpoints"},
        {"name": "Items", "description": "Operations with items (CRUD)"},
        {"name": "Users", "description": "Operations with users"}
    ])


# Register the routers
app.include_router(scm_router, prefix="/scm", tags=["SCM Module"])
# app.include_router(user_router, prefix="/users", tags=["User Module"])

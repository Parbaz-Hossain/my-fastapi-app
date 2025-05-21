from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import models

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="My FastAPI App",
    description="A beginner-friendly API for learning FastAPI in Python!",
    version="1.1.0",
    openapi_tags=[
        {"name": "General", "description": "General or health check endpoints"},
        {"name": "Items", "description": "Operations with items (CRUD)"},
        {"name": "Users", "description": "Operations with users"}
    ])

# Health check endpoints
@app.get("/", tags=["General"])
def read_root():
    return {"message": "Hello, FastAPI!"}

# region Item endpoints

@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/", tags=["Items"])
def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

# endregion

# region User APIs

# Get user
@app.get("/users/{user_id}", tags=["Users"])
def read_user(user_id: int, q: str = None):
    return {"ID": user_id, "query": q}

# Create user
@app.post("/users", tags=["Users"])
def create_user(user: dict):
    return {"user":user}

# endregion

# region Product Category APIs

@app.get("/product_categories", tags=["Product Categories"])
def get_product_categories(db: Session = Depends(get_db)):
    product_categories = db.query(models.ProductCategory).all()
    return product_categories

# endregion
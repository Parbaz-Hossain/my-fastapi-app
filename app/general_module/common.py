



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

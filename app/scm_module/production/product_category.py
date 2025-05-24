from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import app.scm_module.production.schemas as schemas
import app.scm_module.production.models as models
from app.scm_module.production.database import db_operations

router = APIRouter()

# region Product Category APIs

@router.get("/product_category/product_categories", response_model=list[schemas.ProductCategoryResponse])
def get_product_categories(db: Session = Depends(get_db)):
    product_categories = db.query(models.ProductCategory).order_by(models.ProductCategory.id.desc()).all()
    return product_categories

@router.get("/product_category/{category_id}", response_model=schemas.ProductCategoryResponse)
def get_product_category(category_id: int, db: Session = Depends(get_db)):
    product_category = db.query(models.ProductCategory).filter(models.ProductCategory.id == category_id).first()
    if product_category is None:
        return {"error": "Product category not found"}
    return product_category

@router.post("/product_category/save_product_category")
def save_product_category(product_category: schemas.ProductCategoryCreate, db: Session = Depends(get_db)):
    try:
        result = db_operations.save_product_category(product_category, db)
        if result == 200:
            return {"status_code": 200, "message": "Product category saved successfully"}
        else:
            return {"status_code": 400,  "error": "Failed to save product category"}

    except Exception as e:
        return {"status_code": 500,  "Internal server error": str(e)}
    

@router.put("/product_category/update_product_category")
def update_product_category(product_category: schemas.ProductCategoryUpdate, db: Session = Depends(get_db)):
    try:
        result = db_operations.update_product_category(product_category, db)
        if result == 200:
            return {"status_code": 200, "message": "Product category updated successfully"}
        else:
            return {"status_code": 400, "error": "Failed to update product category"}
        
    except Exception as e:
        return {"status_code": 500, "Internal server error": str(e)}

@router.delete("/product_category/delete_product_category/{category_id}")
def delete_product_category(category_id: int, db: Session = Depends(get_db)):
    try:
        result = db_operations.delete_product_category(category_id, db)
        if result == 200:
            return {"status_code": 200, "message": "Product category deleted successfully"}
        else:
            return {"status_code": 404, "error": "Product category not found"}
        
    except Exception as e:
        return {"status_code": 500, "Internal server error": str(e)}

# endregion
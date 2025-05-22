from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import app.scm_module.production.models as models

router = APIRouter()

# region Product Category APIs

@router.get("/product_categories")
def get_product_categories(db: Session = Depends(get_db)):
    product_categories = db.query(models.ProductCategory).all()
    return product_categories

# endregion
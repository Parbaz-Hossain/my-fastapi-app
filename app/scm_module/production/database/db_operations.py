from app.scm_module.production import models
from sqlalchemy.orm import Session


# region Product Category 

def save_product_category(product_category, db: Session):
    new_category = models.ProductCategory(**product_category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return 200

def update_product_category(product_category, db: Session):
    existing_category = db.query(models.ProductCategory).filter(models.ProductCategory.id == product_category.id).first()
    if not existing_category:
        return 404  # Not Found

    for key, value in product_category.dict().items():
        setattr(existing_category, key, value)

    db.commit()
    db.refresh(existing_category)
    return 200

def delete_product_category(category_id: int, db: Session):
    existing_category = db.query(models.ProductCategory).filter(models.ProductCategory.id == category_id).first()
    if not existing_category:
        return 404  # Not Found

    db.delete(existing_category)
    db.commit()
    return 200  

# endregion
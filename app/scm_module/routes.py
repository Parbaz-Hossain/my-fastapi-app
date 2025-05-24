from fastapi import APIRouter
from app.scm_module.production import product_category

router = APIRouter()

# Register individual  SCM Module components as routers
router.include_router(product_category.router)

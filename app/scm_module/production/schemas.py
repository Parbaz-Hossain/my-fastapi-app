from pydantic import BaseModel


class ProductCategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    remarks: str | None = None

    class Config:
        from_attributes = True

class ProductCategoryCreate(BaseModel):
    id : int
    name: str
    description: str | None = None
    remarks: str | None = None

class ProductCategoryUpdate(BaseModel):
    id: int 
    name: str
    description: str | None = None
    remarks: str | None = None

    class Config:
        from_attributes = True
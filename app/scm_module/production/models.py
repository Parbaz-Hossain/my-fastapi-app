from sqlalchemy import Column, Integer, String, DateTime
from database import Base

# region Product Category

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    remarks = Column(String)

# endregion
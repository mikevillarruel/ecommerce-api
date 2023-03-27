from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float

from .base import Base


class ProductEntity(Base):
    __tablename__ = "product"

    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(64))
    price = Column(Float(2))
    stock = Column(Integer)


class Product(BaseModel):
    id: int
    user_id: int
    name: str
    price: float
    stock: int


class ProductCreate(BaseModel):
    user_id: int
    name: str
    price: float
    stock: int


class ProductUpdate(BaseModel):
    name: str | None
    price: float | None
    stock: int | None

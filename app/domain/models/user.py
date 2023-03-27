from pydantic import BaseModel
from sqlalchemy import Column, String

from .base import Base


class UserEntity(Base):
    __tablename__ = "user"

    email = Column(String(128), unique=True)
    password = Column(String(256))


class User(BaseModel):
    id: int
    email: str
    password: str


class UserCreate(BaseModel):
    email: str
    password: str

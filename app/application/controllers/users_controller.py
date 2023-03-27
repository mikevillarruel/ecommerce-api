from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.di import get_users_service
from app.domain.interfaces import IUsersService
from app.domain.models import User, UserCreate

users_router = APIRouter()


@users_router.get("/{email}", response_model=User | dict)
def get_by_email(email: str, service: IUsersService = Depends(get_users_service)) -> User | dict:
    note = service.get_by_email(email)
    if note:
        return note
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")


@users_router.post("/", response_model=User)
def add(user: UserCreate, service: IUsersService = Depends(get_users_service)) -> User:
    try:
        return service.add(user)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.EXPECTATION_FAILED, detail=f"{e.__str__()}")

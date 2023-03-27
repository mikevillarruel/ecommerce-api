from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.di import get_products_service
from app.domain.interfaces import IProductsService
from app.domain.models import Product, ProductCreate, ProductUpdate

products_router = APIRouter()


@products_router.get("/", response_model=list[Product])
def get(service: IProductsService = Depends(get_products_service)) -> list[Product]:
    return service.get()


@products_router.get("/{id}", response_model=Product | dict)
def get_by_id(id: int, service: IProductsService = Depends(get_products_service)) -> Product | dict:
    product = service.get_by_id(id)
    if product:
        return product
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")


@products_router.post("/", response_model=Product)
def add(product: ProductCreate, service: IProductsService = Depends(get_products_service)) -> Product:
    try:
        return service.add(product)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.EXPECTATION_FAILED, detail=f"{e.__str__()}")


@products_router.put("/{id}", response_model=Product)
def update(id: int, product: ProductUpdate, service: IProductsService = Depends(get_products_service)) -> Product:
    product = service.update(id, product)
    if product:
        return product
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")


@products_router.delete("/{id}", response_model=dict)
def delete(id: int, service: IProductsService = Depends(get_products_service)) -> dict:
    return {
        "is_deleted": service.delete(id)
    }

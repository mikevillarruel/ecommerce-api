from abc import ABC, abstractmethod

from app.domain.models import Product, ProductCreate, ProductUpdate


class IProductsService(ABC):

    @abstractmethod
    def get(self) -> list[Product]:
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def add(self, product: ProductCreate) -> Product:
        pass

    @abstractmethod
    def update(self, id: int, product: ProductUpdate) -> Product:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass

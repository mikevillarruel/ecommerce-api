from app.domain.interfaces import IProductsRepository, IProductsService
from app.domain.models import Product, ProductCreate, ProductUpdate


class ProductsService(IProductsService):

    def __init__(self, repository: IProductsRepository):
        self.repository = repository

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get(self) -> list[Product]:
        return self.repository.get()

    def add(self, product: ProductCreate) -> Product:
        return self.repository.add(product)

    def update(self, id: int, product: ProductUpdate) -> Product:
        return self.repository.update(id, product)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)

from sqlalchemy import select, insert, update, delete

from app.domain.interfaces import IProductsRepository
from app.domain.models import Product, ProductCreate, ProductUpdate
from app.domain.models import ProductEntity, UserEntity
from app.infrastructure.db_connector import DB
from app.utils.exceptions import CustomException


class ProductsRepository(IProductsRepository):

    def __init__(self, db: DB):
        self.db = db

    def get(self) -> list[Product]:
        result = self.db.conn.execute(select(ProductEntity).order_by('id')).all()
        my_list: list[Product] = []
        for item in result:
            my_list.append(Product(**item._asdict()))
        return my_list

    def get_by_id(self, id: int) -> Product:
        result = self.db.conn.execute(
            select(ProductEntity).where(ProductEntity.id == id)
        ).first()
        return Product(**result._asdict()) if result else None

    def add(self, product: ProductCreate) -> Product:
        if not self.db.conn.execute(select(UserEntity).where(UserEntity.id == product.user_id)).first():
            raise CustomException("a user with this id doesn't exist")

        result = self.db.conn.execute(
            insert(ProductEntity).values(product.dict(exclude_unset=True))
        ).inserted_primary_key[0]
        self.db.conn.commit()
        return self.get_by_id(result)

    def update(self, id: int, product: ProductUpdate) -> Product:
        result = self.db.conn.execute(
            update(ProductEntity).where(ProductEntity.id == id).values(product.dict(exclude_unset=True))
        )
        self.db.conn.commit()
        return self.get_by_id(id)

    def delete(self, id: int) -> bool:
        result = self.db.conn.execute(delete(ProductEntity).where(ProductEntity.id == id))
        self.db.conn.commit()
        return result.rowcount > 0

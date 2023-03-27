from app.domain.services import UsersService, ProductsService
from app.infrastructure import POSTGRESQL
from app.infrastructure.repositories import UsersRepository, ProductsRepository


def get_users_service() -> UsersService:
    return UsersService(
        get_users_repository()
    )


def get_users_repository() -> UsersRepository:
    return UsersRepository(POSTGRESQL.get_instance())


def get_products_service() -> ProductsService:
    return ProductsService(
        get_products_repository()
    )


def get_products_repository() -> ProductsRepository:
    return ProductsRepository()

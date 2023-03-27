from app.domain.interfaces import IUsersRepository, IUsersService
from app.domain.models import User, UserCreate


class UsersService(IUsersService):

    def __init__(self, repository: IUsersRepository):
        self.repository = repository

    def get_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def add(self, user: UserCreate) -> User:
        return self.repository.add(user)

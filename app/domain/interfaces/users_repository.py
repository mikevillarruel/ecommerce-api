from abc import ABC, abstractmethod

from app.domain.models import User, UserCreate


class IUsersRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def add(self, user: UserCreate) -> User:
        pass

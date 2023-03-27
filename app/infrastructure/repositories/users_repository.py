from sqlalchemy import select, insert

from app.domain.interfaces import IUsersRepository
from app.domain.models import User, UserCreate
from app.domain.models import UserEntity
from app.infrastructure.db_connector import DB
from app.utils.exceptions import CustomException


class UsersRepository(IUsersRepository):

    def __init__(self, db: DB):
        self.db = db

    def get_by_email(self, email: str) -> User:
        result = self.db.conn.execute(
            select(UserEntity).where(UserEntity.email == email)
        ).first()
        return User(**result._asdict()) if result else None

    def add(self, user: UserCreate) -> User:
        if self.db.conn.execute(select(UserEntity).where(UserEntity.email == user.email)).first():
            raise CustomException("a user with this email already exist")

        self.db.conn.execute(
            insert(UserEntity).values(user.dict(exclude_unset=True))
        )
        self.db.conn.commit()
        return self.get_by_email(user.email)

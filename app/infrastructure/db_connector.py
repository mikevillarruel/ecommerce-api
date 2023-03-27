from sqlalchemy import Connection, create_engine

from app.domain.models import Base
from app.utils.env_config import EnvConfig


class DB:
    DB_URL: str = None
    instance: any = None
    conn: Connection = None

    def __init__(self):
        if not self.DB_URL:
            raise ValueError("DB_URL can't be empty")
        engine = create_engine(self.DB_URL)
        Base.metadata.create_all(engine)
        self.conn = engine.connect()

    @classmethod
    def get_instance(cls):
        if cls.conn is None:
            cls.instance = cls()
        return cls.instance


class POSTGRESQL(DB):
    DB_URL = EnvConfig.DB_URL

# class SQLITE(DB):
#     DB_URL = EnvConfig.TEST_DB_URL

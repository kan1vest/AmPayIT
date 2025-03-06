
from asyncpg import connect
from config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


async_engine = create_async_engine(
  url=settings.DATABASE_URL_asyncpg,
  echo=False
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):            # создаем класс базе для объявления всех моделей 
    repr_cols_num = 3
    repr_cols = tuple()
    
    def __repr__(self):
        # Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"



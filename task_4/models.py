from typing import Annotated
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, DateTime, Integer, String, func, text
from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class WorkersORM(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)
    salary = Column(Integer)
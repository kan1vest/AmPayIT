from typing import Annotated
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, DateTime, Integer, String, func, text
from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class OrdersOrm(Base):
    __tablename__ = "orders"

    id: Mapped[intpk]
    customer_id = Column(Integer)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    amount: Mapped[int]
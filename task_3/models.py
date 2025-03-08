from typing import Annotated
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, text
from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class OrdersOrm(Base):
    __tablename__ = "orders"

    id: Mapped[intpk]
    customer_id = Column(Integer)
    order_date: Mapped[created_at]
    amount: Mapped[int]
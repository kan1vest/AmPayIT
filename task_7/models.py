from more_itertools import quantify
from sqlalchemy import Column, Integer, String
from database import Base



class ProductsOrm(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
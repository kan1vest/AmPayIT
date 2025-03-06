from sqlalchemy import Column, Integer, String
from database import Base



class EmployseeOrm(Base):
    __tablename__ = "employsees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String, unique=True, index=True)
    salary = Column(String)
from sqlalchemy import Column, Integer, String
from database import Base



class EmployeesOrm(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String, index=True)
    salary = Column(Integer)
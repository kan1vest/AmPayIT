from pydantic import BaseModel




class EmployUpdateShaema(BaseModel):
   name: str
   salary: int
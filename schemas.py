from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: str
    start_date: str
    office: str
    extn: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True

class EmployeeResponse(BaseModel):
    data: list[Employee]

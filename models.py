from sqlalchemy import Boolean, Column, Date, Integer, String

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    position = Column(String, index=True)
    salary = Column(String)
    start_date = Column(String)
    office = Column(String)
    extn = Column(Integer)
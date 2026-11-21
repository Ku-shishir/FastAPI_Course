from sqlalchemy import Column, Integer, String
from database import Base


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    
    
    # department = Column(String,index=True)
    # phone = Column(String,index=True)
    # salary = Column(Integer,index=True)
    # password = Column(String)
    # join_date = Column(Date,index=True)
    # is_active = Column(Boolean,default=True)
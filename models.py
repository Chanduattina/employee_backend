from sqlalchemy import Column, engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    yob = Column(Integer, nullable=False)
    # gender = Column(String(1))

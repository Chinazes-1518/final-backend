from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey, Integer, String, JSON, DateTime, Column


class MyBase(DeclarativeBase):
    pass


class User(MyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

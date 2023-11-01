from sqlalchemy import Boolean, Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from .items import Items


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password=Column(String)
    items = relationship("Items", back_populates="user")

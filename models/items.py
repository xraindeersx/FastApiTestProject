from sqlalchemy import Boolean, Column, Integer, String, ForeignKey,DateTime,func
from database import Base

from sqlalchemy.orm import relationship
# from .user import User

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="items")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
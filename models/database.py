from sqlalchemy import Boolean, String, Integer, Column, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from utils import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    pk = Column(Integer, primary_key=True, unique=True)
    username = Column(String(length=250),  unique=True)
    address = Column(String(length=250), unique=True)
    total_point = Column(String(length=250))

class AddPoint(Base):
    __tablename__ = "addpoint"
    pk = Column(Integer, primary_key=True, unique=True)
    add_point = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    user_id = Column(Integer, ForeignKey("user.pk"), nullable=False)

class RemovePoint(Base):
    __tablename__ = "removepoint"
    pk = Column(Integer, primary_key=True, unique=True)
    remove_point = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    user_id = Column(Integer, ForeignKey("user.pk"), nullable=False)



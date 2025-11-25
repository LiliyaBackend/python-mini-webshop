from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Float)
    image = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    items = Column(String)        # просто текстовое подтверждение заказа
    total = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

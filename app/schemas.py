from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    image: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class OrderCreate(BaseModel):
    items: str
    total: float

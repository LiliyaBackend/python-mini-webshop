from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import Base, engine, SessionLocal
from . import crud
from .routers import products, checkout, users
from . import auth, cart, orders

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Подключаем роутеры
app.include_router(products.router)
app.include_router(checkout.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(orders.router)

# Создаем таблицы и дефолтные товары
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    crud.create_default_products(db)

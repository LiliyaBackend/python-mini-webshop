from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine, SessionLocal
from . import crud
from .routers import products, checkout, users, cart
from . import auth, orders

app = FastAPI()

# Подключаем статику
app.mount("/static", StaticFiles(directory="static"), name="static")

# Шаблоны
templates = Jinja2Templates(directory="app/templates")

# Добавляем templates в объект приложения
app.templates = templates

# Подключаем роутеры
app.include_router(products.router)
app.include_router(checkout.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(orders.router)

# Создаем таблицы и добавляем товары
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    crud.create_default_products(db)

# Главная страница
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

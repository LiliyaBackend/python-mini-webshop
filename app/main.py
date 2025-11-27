from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# База данных и CRUD
from .database import Base, engine, SessionLocal
from . import crud

# Роутеры
from .routers import products, checkout, users
from . import auth, cart, orders

# ───────────────────────────────────────────────

app = FastAPI(title="Simple Shop")

# Подключаем путь к статике
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="app/templates")

# Подключаем роутеры
app.include_router(products.router)
app.include_router(checkout.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(orders.router)

# ───────────────────────────────────────────────
# Создаём таблицы и добавляем дефолтные товары
Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    crud.create_default_products(db)

# ───────────────────────────────────────────────
# Главная страница
@app.get("/")
async def index(re

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine, SessionLocal
from . import crud
from .routers import products, checkout, users
from . import auth, cart, orders

app = FastAPI()

# Статика
app.mount("/static", StaticFiles(directory="static"), name="static")

# Шаблоны
app.templates = Jinja2Templates(directory="app/templates")

# Роутеры
app.include_router(products.router)
app.include_router(checkout.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(orders.router)

# Создаем таблицы и товары
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    crud.create_default_products(db)

@app.get("/")
def index(request):
    return app.templates.TemplateResponse("index.html", {"request": request})

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..database import SessionLocal
from .. import crud

router = APIRouter()

# Создаём Jinja2 шаблоны напрямую здесь
templates = Jinja2Templates(directory="app/templates")

@router.get("/products")
async def products_page(request: Request):
    # Получаем все товары из БД
    with SessionLocal() as db:
        products_list = crud.get_all_products(db)

    return templates.TemplateResponse(
        "products.html",
        {"request": request, "products": products_list}
    )

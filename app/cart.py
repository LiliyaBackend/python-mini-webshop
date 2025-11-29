from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Страница корзины
@router.get("/cart")
async def cart_page(request: Request, db: Session = Depends(get_db)):
    # Пример заглушки корзины
    cart_items = [
        {"name": "product_1", "price": 1, "quantity": 1},
        {"name": "product_2", "price": 2, "quantity": 2},
    ]
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    return templates.TemplateResponse("cart.html", {"request": request, "cart_items": cart_items, "total": total})

# Добавление товара в корзину через форму
@router.post("/cart/add")
async def add_to_cart(
    product_name: str = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db)
):
    # Здесь логика добавления в корзину (пока просто печатаем)
    print(f"Добавляем {quantity} шт. товара {product_name}")
    return {"message": f"{quantity} шт. {product_name} добавлено в корзину"}

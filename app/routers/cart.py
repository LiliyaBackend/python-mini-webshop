from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db  # <- теперь работает

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/cart")
async def cart_page(request: Request, db: Session = Depends(get_db)):
    # Здесь можно использовать db, пока пример с заглушкой
    cart_items = [
        {"name": "product_1", "price": 1, "quantity": 1},
        {"name": "product_2", "price": 2, "quantity": 2},
    ]
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    return templates.TemplateResponse("cart.html", {"request": request, "cart_items": cart_items, "total": total})

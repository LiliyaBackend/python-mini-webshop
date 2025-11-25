from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order/confirm", response_class=HTMLResponse)
def confirm_order(
    name: str = Form(...),
    address: str = Form(...),
    payment: str = Form(...),
    request: Request = None,
    db: Session = Depends(get_db)
):

    # читаем корзину
    cart = request.cookies.get("cart", "").strip(",").split(",")
    products = crud.get_products(db)
    total = 0
    items = []

    for p in products:
        if str(p.id) in cart:
            total += p.price
            items.append(p.name)

    # создаем заказ (очень простая модель)
    order = models.Order(items=", ".join(items), total=total, user_id=1)
    db.add(order)
    db.commit()

    return request.app.templates.TemplateResponse(
        "order_confirm.html",
        {
            "request": request,
            "items": items,
            "total": total,
            "name": name,
            "address": address,
            "payment": payment,
        }
    )

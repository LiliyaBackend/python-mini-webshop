from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("/")
def cart_page(request: Request, db: Session = Depends(get_db)):
    cart_items = crud.get_cart_items(db)
    return request.app.state.templates.TemplateResponse(
        "cart.html",
        {"request": request, "cart_items": cart_items}
    )

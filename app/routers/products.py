from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/products")
def get_products(request: Request, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

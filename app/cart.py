from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/cart/add")
def add_to_cart(product_id: int = Form(...), request: Request = None):
    cart = request.cookies.get("cart", "")
    cart = cart + f"{product_id},"
    response = RedirectResponse("/products", status_code=302)
    response.set_cookie("cart", cart)
    return response

@router.get("/cart/clear")
def clear_cart():
    response = RedirectResponse("/products", status_code=302)
    response.delete_cookie("cart")
    return response

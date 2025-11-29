from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Страница корзины
@router.get("/cart")
async def cart_page(request: Request):
    cart_cookie = request.cookies.get("cart", "")
    # Преобразуем строку "1,2,3," в список
    cart_items_ids = [int(i) for i in cart_cookie.split(",") if i]
    
    # Для примера создаём товары с именами и ценами
    products = {
        1: {"name": "product_1", "price": 1},
        2: {"name": "product_2", "price": 2},
        3: {"name": "product_3", "price": 3},
    }
    
    cart_items = []
    total = 0
    for pid in cart_items_ids:
        product = products.get(pid)
        if product:
            cart_items.append({"name": product["name"], "price": product["price"], "quantity": 1})
            total += product["price"]
    
    return templates.TemplateResponse("cart.html", {"request": request, "cart_items": cart_items, "total": total})

# Добавление товара в корзину
@router.post("/cart/add")
async def add_to_cart(request: Request, product_id: int = Form(...)):
    cart = request.cookies.get("cart", "")
    cart = cart + f"{product_id},"
    response = RedirectResponse("/cart", status_code=302)  # Перенаправляем на страницу корзины
    response.set_cookie("cart", cart)
    return response

# Очистка корзины
@router.get("/cart/clear")
async def clear_cart():
    response = RedirectResponse("/cart", status_code=302)
    response.delete_cookie("cart")
    return response

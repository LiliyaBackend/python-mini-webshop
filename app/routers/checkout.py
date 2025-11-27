from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Страница оформления заказа
@router.get("/checkout")
async def checkout_page(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})

# Подтверждение заказа
@router.post("/checkout")
async def checkout_submit(request: Request, name: str = Form(...), address: str = Form(...)):
    # В учебном проекте просто показываем текст
    order_text = f"Заказ для {name}, адрес доставки: {address}"
    return templates.TemplateResponse("order_confirm.html", {"request": request, "order_text": order_text})

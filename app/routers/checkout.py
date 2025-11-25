from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/checkout", response_class=HTMLResponse)
def checkout_page(request: Request):
    return request.app.templates.TemplateResponse(
        "checkout.html",
        {"request": request}
    )

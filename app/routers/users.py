from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Заглушка: простой login без БД
@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    # Простейшая проверка (в учебном проекте)
    if username == "user" and password == "pass":
        response = RedirectResponse(url="/", status_code=302)
        # Здесь можно добавить cookie/session
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Неверные данные"})

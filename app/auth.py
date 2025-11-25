from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return request.app.templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(username: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=username).first()
    if not user:
        user = models.User(username=username, password="123")
        db.add(user)
        db.commit()
    return RedirectResponse("/", status_code=302)

@router.get("/logout")
def logout():
    return RedirectResponse("/", status_code=302)

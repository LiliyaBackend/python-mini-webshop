from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/user")
def user_home():
    return RedirectResponse("/login")

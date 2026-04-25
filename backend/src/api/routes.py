from fastapi import APIRouter, Depends
from services.auth_service import login_user

router = APIRouter()

@router.post("/login")
def login(data: dict):
    return login_user(data)

@router.get("/users")
def get_users():
    return [{"id": 1, "email": "user@gmail.com"}]

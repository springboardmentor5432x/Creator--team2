from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import RegisterRequest
from app.schemas.login_schema import LoginRequest
from app.services.auth_service import register_user, login_user, login_user_json
from app.auth.oauth2 import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):
    return register_user(user, db)


@router.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_user_json(user, db)


@router.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": f"{current_user.first_name} {current_user.last_name}".strip() or current_user.first_name,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
        "role": current_user.role
    }

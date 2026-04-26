from fastapi import APIRouter
from app.schemas import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/validate")
def validate_user(user: User):
    return {"message": "Пользователь валиден", "user": user.dict()}
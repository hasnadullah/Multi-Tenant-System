from fastapi import APIRouter
from app.schemas.user_schema import UserSchema
from app.controllers.user_controller import register

router = APIRouter()

@router.post("/register")
def register_route(data: UserSchema):
    register(data)
    return {"message": "User registered"}

from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserSchema
from app.schemas.create_user_schema import CreateUserSchema
from app.controllers.user_controller import register, create_user
from app.core.tenant import get_current_user

router = APIRouter()

# Public – creates new tenant + admin
@router.post("/register")
def register_route(data: UserSchema):
    register(data)
    return {"message": "Admin registered, tenant created"}

# Admin-only – creates user in same tenant
@router.post("/create")
def create_user_route(
    data: CreateUserSchema,
    admin_user: dict = Depends(get_current_user)
):
    create_user(data, admin_user)
    return {"message": "User created successfully"}

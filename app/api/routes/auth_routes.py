from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import LoginSchema
from app.services.auth_service import login_user

router = APIRouter()

@router.post("/login")
def login_route(data: LoginSchema):
    token = login_user(data.email, data.password)
    if not token:
        raise HTTPException(401, "Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import LoginSchema
from app.repositories.user_repository import get_user_by_email
from app.utils.password_utils import verify_password
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login_route(data: LoginSchema):
    user = get_user_by_email(data.email)
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(str(user["_id"]))
    return {"access_token": token, "token_type": "bearer"}

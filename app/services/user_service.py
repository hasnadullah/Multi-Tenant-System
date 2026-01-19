from app.repositories.user_repository import create_user, get_user_by_email
from app.utils.password_utils import hash_password
from fastapi import HTTPException
import uuid

def register_user(email: str, password: str):
    if get_user_by_email(email):
        raise HTTPException(400, "Email already exists")

    tenant_id = str(uuid.uuid4())

    user = {
        "email": email,
        "password": hash_password(password),
        "tenant_id": tenant_id,
        "role": "admin"
    }
    create_user(user)

def create_user_by_admin(email: str, password: str, role: str, admin_user: dict):
    if admin_user["role"] != "admin":
        raise HTTPException(403, "Only admin can create users")

    if get_user_by_email(email):
        raise HTTPException(400, "Email already exists")

    user = {
        "email": email,
        "password": hash_password(password),
        "tenant_id": admin_user["tenant_id"],
        "role": role
    }
    create_user(user)

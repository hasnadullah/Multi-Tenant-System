from app.repositories.user_repository import get_user_by_email
from app.utils.password_utils import verify_password
from app.core.security import create_access_token

def login_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        return None

    return create_access_token({
        "user_id": str(user["_id"]),
        "tenant_id": user["tenant_id"],
        "role": user["role"]
    })

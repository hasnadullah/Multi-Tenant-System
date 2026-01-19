from app.repositories.user_repository import create_user
from app.utils.password_utils import hash_password

def register_user(email: str, password: str):
    user = {
        "email": email,
        "password": hash_password(password)
    }
    create_user(user)

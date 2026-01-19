from app.services.user_service import register_user

def register(data):
    register_user(data.email, data.password)

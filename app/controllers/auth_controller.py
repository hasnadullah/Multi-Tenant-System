from app.services.auth_service import login_user

def login(data):
    return login_user(data.email, data.password)

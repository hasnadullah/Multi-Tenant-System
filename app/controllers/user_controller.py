from app.services.user_service import register_user, create_user_by_admin

def register(data):
    register_user(data.email, data.password)

def create_user(data, admin_user):
    create_user_by_admin(
        email=data.email,
        password=data.password,
        role=data.role,
        admin_user=admin_user
    )

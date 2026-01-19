from app.db.mongo import db
users = db.users

def get_user_by_email(email: str):
    return users.find_one({"email": email})

def create_user(user: dict):
    return users.insert_one(user)

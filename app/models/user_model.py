def user_entity(user):
    return {
        "id": str(user["_id"]),
        "email": user["email"]
    }

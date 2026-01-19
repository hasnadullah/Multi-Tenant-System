from app.repositories.product_repository import *
from app.core.permissions import require_roles

def add_product(name, user):
    require_roles(["admin", "manager"], user["role"])
    create_product({
        "name": name,
        "tenant_id": user["tenant_id"],
        "created_by": user["user_id"]
    })

def list_products(user):
    return get_products_by_tenant(user["tenant_id"])

def edit_product(product_id, name, user):
    require_roles(["admin", "manager"], user["role"])
    if not update_product(product_id, user["tenant_id"], name):
        raise Exception("Product not found")

def remove_product(product_id, user):
    require_roles(["admin"], user["role"])
    if not delete_product(product_id, user["tenant_id"]):
        raise Exception("Product not found")

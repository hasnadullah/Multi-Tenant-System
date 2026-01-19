from app.repositories.product_repository import create_product, get_products_by_owner, update_product, delete_product

def add_product(name: str, owner_id: str):
    create_product({
        "name": name,
        "owner_id": owner_id
    })

def list_products(owner_id: str):
    return get_products_by_owner(owner_id)

def edit_product(product_id: str, owner_id: str, new_name: str):
    updated = update_product(product_id, owner_id, new_name)
    if not updated:
        raise Exception("Product not found or you are not the owner")

def remove_product(product_id: str, owner_id: str):
    deleted = delete_product(product_id, owner_id)
    if not deleted:
        raise Exception("Product not found or you are not the owner")
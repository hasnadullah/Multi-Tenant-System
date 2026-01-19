from app.services.product_service import add_product, list_products, edit_product, remove_product



def create(name: str, user_id: str):
    add_product(name, user_id)

def get_all(user_id: str):
    return list_products(user_id)

def update(product_id: str, new_name: str, user_id: str):
    edit_product(product_id, user_id, new_name)

def delete(product_id: str, user_id: str):
    remove_product(product_id, user_id)
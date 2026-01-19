from app.services.product_service import *

def create(name, user):
    add_product(name, user)

def get_all(user):
    return list_products(user)

def update(product_id, name, user):
    edit_product(product_id, name, user)

def delete(product_id, user):
    remove_product(product_id, user)

from bson import ObjectId
from app.db.mongo import db

products = db.products

def create_product(product: dict):
    products.insert_one(product)

def get_products_by_tenant(tenant_id: str):
    return [
        {"id": str(p["_id"]), "name": p["name"]}
        for p in products.find({"tenant_id": tenant_id})
    ]

def update_product(product_id, tenant_id, name):
    return products.update_one(
        {"_id": ObjectId(product_id), "tenant_id": tenant_id},
        {"$set": {"name": name}}
    ).modified_count

def delete_product(product_id, tenant_id):
    return products.delete_one(
        {"_id": ObjectId(product_id), "tenant_id": tenant_id}
    ).deleted_count

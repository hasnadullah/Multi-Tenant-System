from bson import ObjectId
from app.db.mongo import db

products = db.products

def create_product(product: dict):
    return products.insert_one(product)

def get_products_by_owner(owner_id: str):
    # Convert _id to string for each document
    result = []
    for p in products.find({"owner_id": owner_id}):
        result.append({
            "id": str(p["_id"]),
            "name": p["name"],
            "owner_id": p["owner_id"]
        })
    return result

def update_product(product_id: str, owner_id: str, new_name: str):
    res = products.update_one(
        {"_id": ObjectId(product_id), "owner_id": owner_id},
        {"$set": {"name": new_name}}
    )
    return res.modified_count

def delete_product(product_id: str, owner_id: str):
    res = products.delete_one(
        {"_id": ObjectId(product_id), "owner_id": owner_id}
    )
    return res.deleted_count
def product_entity(product):
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "owner_id": product["owner_id"]
    }

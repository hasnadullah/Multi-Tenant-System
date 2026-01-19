def product_entity(product):
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "tenant_id": product["tenant_id"],
        "created_by": product["created_by"]
    }

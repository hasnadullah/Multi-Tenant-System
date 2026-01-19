from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product_schema import ProductSchema
from app.controllers.product_controller import *
from app.core.tenant import get_current_user

router = APIRouter()

@router.post("/")
def create_product(data: ProductSchema, user=Depends(get_current_user)):
    create(data.name, user)
    return {"message": "Product created"}

@router.get("/")
def list_products(user=Depends(get_current_user)):
    return get_all(user)

@router.put("/{product_id}")
def update_product_route(product_id: str, data: ProductSchema, user=Depends(get_current_user)):
    update(product_id, data.name, user)
    return {"message": "Product updated"}

@router.delete("/{product_id}")
def delete_product_route(product_id: str, user=Depends(get_current_user)):
    delete(product_id, user)
    return {"message": "Product deleted"}

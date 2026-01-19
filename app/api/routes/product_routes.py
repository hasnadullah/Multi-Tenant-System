from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product_schema import ProductSchema
from app.controllers.product_controller import create, get_all, update, delete
from app.core.tenant import get_current_user

router = APIRouter()

@router.post("/")
def create_product(data: ProductSchema, user_id: str = Depends(get_current_user)):
    create(data.name, user_id)
    return {"message": "Product added"}

@router.get("/")
def list_products(user_id: str = Depends(get_current_user)):
    # Now will safely return list
    return get_all(user_id)

@router.put("/{product_id}")
def update_product_route(product_id: str, data: ProductSchema, user_id: str = Depends(get_current_user)):
    try:
        update(product_id, data.name, user_id)
        return {"message": "Product updated"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{product_id}")
def delete_product_route(product_id: str, user_id: str = Depends(get_current_user)):
    try:
        delete(product_id, user_id)
        return {"message": "Product deleted"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
from fastapi import FastAPI, Depends, Security
from fastapi.security import HTTPBearer
from app.api.routes import auth_routes, user_routes, product_routes

app = FastAPI(title="Multi-Tenant Learning App")

# Define a reusable Bearer scheme
bearer_scheme = HTTPBearer()

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])

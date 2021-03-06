from fastapi import FastAPI
from .routers import api_root
from .routers.v1 import api_chains, api_products, api_locations


def api_registry(app: FastAPI):
    app.include_router(api_root.router, prefix="/v1")
    app.include_router(api_chains.router, prefix="/v1", tags=["chains"])
    app.include_router(api_products.router, prefix="/v1", tags=["products"])
    app.include_router(api_locations.router, prefix="/v1", tags=["locations"])


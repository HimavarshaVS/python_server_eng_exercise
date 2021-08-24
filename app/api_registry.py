from fastapi import FastAPI
from .routers import api_root
from .routers.v1 import api_chains


def api_registry(app: FastAPI):
    app.include_router(api_root.router, prefix="/v1")
    app.include_router(api_chains.router, prefix="/v1")

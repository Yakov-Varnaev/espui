from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import router


def create_app() -> FastAPI:
    v1_router = APIRouter(prefix='/api/v1')
    v1_router.include_router(router)
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
    )
    app.include_router(router=v1_router)
    return app

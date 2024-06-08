from fastapi import FastAPI

from src.controllers import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=router)
    return app

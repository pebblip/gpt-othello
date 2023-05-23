from fastapi import APIRouter, FastAPI

from .othello import router

api_router = APIRouter()

api_router.include_router(
    router,
    tags=["オセロ"],
)

app = FastAPI(title="オセロ")

app.include_router(api_router)

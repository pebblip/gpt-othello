from fastapi import APIRouter, FastAPI

from .gpt import router as gpt_router
from .othello import router as othello_router

api_router = APIRouter()

api_router.include_router(
    othello_router,
    tags=["Othello"],
)

api_router.include_router(
    gpt_router,
    tags=["GPT"],
)

app = FastAPI(title="Othello Game")

app.include_router(api_router)

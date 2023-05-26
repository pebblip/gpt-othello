from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import app as api

app = FastAPI()

app.mount("/api", api)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

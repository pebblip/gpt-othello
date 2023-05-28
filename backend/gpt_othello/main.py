import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import app as api

_stage = os.getenv("STAGE", "dev")

_root_path = '' if _stage == 'dev' else '/prod'

app = FastAPI(root_path=_root_path)

app.mount("/api", api)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

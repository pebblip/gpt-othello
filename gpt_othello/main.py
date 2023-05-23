from fastapi import FastAPI

from .api import app as api

app = FastAPI()

app.mount("/api", api)

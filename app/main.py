from functools import lru_cache

from fastapi import FastAPI
from .config import Config

app = FastAPI()


@lru_cache
def get_configs():
    return Config()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

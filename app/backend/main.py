from typing import Union
import uvicorn
from fastapi import FastAPI
from utils import get_tw_time


app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/time")
def get_time():
    return f"Time {get_tw_time()}"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

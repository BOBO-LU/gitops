from typing import Union
import uvicorn
from fastapi import FastAPI
import pytz
import datetime as dt

app = FastAPI()


@app.get("/")
def read_root():
    tw = pytz.timezone('Asia/Taipei')
    twdt = tw.localize(dt.datetime.now()).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return {"Hello": "World.", "Time": f"{twdt}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

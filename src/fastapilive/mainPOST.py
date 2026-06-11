from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


class Item(BaseModel):
    name : str
    description : str | None = None #OPZIONALE
    price : float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return "hello world"


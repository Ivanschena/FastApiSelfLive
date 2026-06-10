from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"username":"me"}

@app.get("/users/{user_id}")
async def read_user_me(user_id:int):
    return {"user_id":user_id}


class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}


fake_items_db = [{"item_name": "prodotto1"}, {"item_name": "prodotto2"}, {"item_name": "Baz3"}] 


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

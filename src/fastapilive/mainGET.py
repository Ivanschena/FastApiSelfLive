from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}


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


fake_items_db = [{"item_name": "prodotto1"}, {"item_name": "prodotto2"}, {"item_name": "Prodotto3"},{"item_name": "Prodotto4"},{"item_name": "Calza"}] 


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]




#aggiungi un posto a tavola parametro q

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}




#aggiungi 2 posti a tavola anche un booleano
#converte l'1 in true e lo 0 in false ma lui comunque converte
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):#SI PARTE DA FALSE
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:  #CONVERSIONE CON IF NOT
        item.update({"description": "Questo è un elemento con una descrizione lunga."})
    return item

#PIU VARIABILI NELL'URI
#IMPORTANTE il .updare aggiorna il dizionario dei campi 

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#         item = {"item_id": item_id, "owner_id": user_id}
#         if q:
#             item.update({"q": q})#AGGIORNA I DIZIONARI
#         if not short:
#             item.update({"description": "Questo è un elemento con una descrizione lunga."})
#         return item

#IL NEEEDY
#IL REQUIRED

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy} 
#     return item


#ALL IN ONE TUTTI I CASI 

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit} 
    return item




# ∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫∫


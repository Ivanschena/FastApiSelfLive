from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel, Field


#main delle REQUEST BODY

app = FastAPI()


# class Item(BaseModel):
#     name : str
#     description : str | None = None #OPZIONALE
#     price : float
#     tax: float | None = None


class Item(BaseModel):
    name: str
    app
    description: str | None = Field(None, title="Descrizione dell'elemento", max_length=300)
    price: float = Field(..., gt=0, description="Il prezzo dell'elemento, deve essere maggiore di zero")
    tax: float | None = None




@app.get("/")
async def root():
    return "hello world"

#INSERIRE UN ARTICOLO ENTITA' DI ITEM 
#PERFETTA INTEGRAZIONE DI PYDANTIC

# @app.post("/items/")
# async def create_item(item: Item):
#     return item


#elaborazione senza passare dal db solo update

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump() # Converte l'oggetto in un dizionario 
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#       return {"item_id": item_id, **item.model_dump()}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()} 
    if q:
        result.update({"q": q}) 
    return result
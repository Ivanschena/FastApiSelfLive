from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import Field,BaseModel


app = FastAPI()


#fixedquery pattern
#annotated 
#non crea l'entità errore 422 unprocessable se non rispetta l'interfaccia 

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^chequeryquesta$")] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]} 
    if q:
        results.update({"q": q})
    return results


#VALIDAZIONE DEI PARAMETRI ITEM ID


@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="ID dell'elemento", gt=0, le=1000)]):
    return {"item_id": item_id}


class FilterParams (BaseModel):
    #QUESTO PER EVITARE L'INJECTION
    model_config = {"extra": "forbid"} #per non accettare altri dati in input
    limit: int = Field(100, gt=0, le=100) 
    offset: int = Field(0, ge=0)  #non l'ho capito
    order_by: str = "created_at" #qui ce ne stavano altri 
    tags: list[str] = []
    
    
@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name: str
    description: str|None=None
    price: float
    tags: list[str]=[]

@app.post("/item/")
async def create_item(item: Item)->Item:
    return item

@app.get("/item/")
async def read_item()->list[Item]:
    return[
        Item(name="Portal Gun",price=100),
        Item(name="Spirit",price=50.5),
    ]


from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str#default
    description: str |None=None#optional
    price: float#default
    tax: float|None=None#optional

app=FastAPI()
# @app.post("/item/")
# async def create_item(item:Item):
#     return item

#use the model
# @app.post("/item")
# async def create_item(item:Item):
#     item_dict=item.model_dump()#converts item(Pydantic object) to Python dict
#     if item.tax is not None:
#         price_with_tax=item.price+item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

#Request body+path parameters
# @app.put("/item/{item_id}")
# async def update_item(item_id:int,item:Item):
#     return{"item_id":item_id,**item.model_dump()}#** unpacks the dictionary into keyword arguments.

#Request+path+query
@app.put("/item/{item_id}")
async def update_item(item_id:int,item:Item,q:str|None=None):
    result={"item_id":item_id,**item.model_dump()}
    if q:
        result.update({"q":q})
    return result
    
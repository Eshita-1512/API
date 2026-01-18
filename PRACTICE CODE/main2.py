from fastapi import FastAPI
app=FastAPI()
# fake_items=[{"item_name":"Esh"},{"item_name":"Basketball"},{"item_name":"College"}]
# @app.get("/item/")
# async def read_item(skip:int=0, limit:int=10):
#     return fake_items[skip:skip+limit]
#query parameters are skip:with a value of 0 and limit:with value of 10

#query parameter type conversion
# @app.get("/item/{item_id}")
# async def read_item(item_id:str, q:str| None = None,short:bool = False):
#     item={"item_id":item_id}
#     if q:
#         item.update({"q":q})
#     if not short:
#         item.update({"description":"Thos os an amazing item that has a long description"})
#     return item

#required query parameters
@app.get("/item/{item_id}")
async def read_user_item(item_id:str,needy:str):
    item={"item_id":item_id,"needy":needy}
    return item

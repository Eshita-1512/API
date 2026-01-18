
from enum import Enum
# app=FastAPI()

# @app.get("/item/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

#path parameters with types
# @app.get("/item/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#in this case item_id is declared to be int
from fastapi import FastAPI
class ModelName(str,Enum):
    #name of ML models
    alexnet="alexnet"
    resnet="resnet"
    lenet="lenet"
app=FastAPI()
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep learning FTW"}
    if model_name == ModelName.lenet:
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name":model_name,"messgae":"Have some residuals"}


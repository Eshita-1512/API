from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app=FastAPI()
# class UserIn(BaseModel):
#     username: str
#     email: EmailStr
#     password: str
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#
# @app.post("/user", response_model=UserOut)
# def create_user(user: UserIn)->Any:#Any is used to tell that return can be of any type
#     return user

#approach 2
class BaseUser(BaseModel):
    username: str
    email: EmailStr
class UserIn(BaseUser):
    password: str

@app.post("/user/")
async def create_user(user: UserIn)->BaseUser:
    return user

from fastapi import FastAPI, Response, Depends, Cookie
from fastapi import Form
from pydantic import BaseModel
from typing_extensions import Annotated
import random

app = FastAPI()

fake_bd = {
    "Igor": {
        "name": "Igor",
        "password": "abc123",
        "session_token": None,
    },
    "Mike": {
        "name":"Mike",
        "password": "aaa",
        "session_token":None,
    }
}


class User(BaseModel):
    name: str
    password: str


def authenticate(bd, username: str, password: str):
    if username in bd:
        if bd[username]["password"] == password:
            return True


def gener_value():
    return str(random.random())


username_form = Form()
password_form = Form()




@app.put("/login")
def login(username: str = username_form, password: str = password_form, response: Response,
          unic: Annotated[str, Depends(gener_value)]):
    if authenticate(fake_bd, username, password):
        response.set_cookie(key="session_token", secure=True, value=unic)
        fake_bd[username]["session_token"] = unic
        return {"a": "good"}

@app.get("/user")
def get_user(session_token = Cookie()):
    if fake_bd[username_form]["session_token"] == session_token:
        user = fake_bd[username_form]
        return User(**user)



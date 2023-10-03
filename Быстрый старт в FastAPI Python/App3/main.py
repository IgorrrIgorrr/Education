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
        "id": "1",
    },
    "Mike": {
        "name":"Mike",
        "password": "aaa",
        "id":"2",
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


@app.put("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()], response: Response,
          unic: Annotated[str, Depends(gener_value)]):
    if authenticate(fake_bd, username, password):
        response.set_cookie(key="session_token", secure=True, value=unic)
        return {"a": "good"}

@app.get("/user")
def get_user(session_token = Cookie(), id: int = Cookie()):
    if session_token == unic:
        us_dict = fake_bd[us]
        return {"session_token": session_token}



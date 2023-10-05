from fastapi import FastAPI, Response, Depends, Cookie
from fastapi import Form, HTTPException, status
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
        "name": "Mike",
        "password": "aaa",
        "session_token": None,
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
def login(unic: Annotated[str, Depends(gener_value)], response: Response, username: str = username_form,
          password: str = password_form):
    if not authenticate(fake_bd, username, password):
        raise HTTPException(status_code=404, detail="You are not registrated")
    else:
        response.set_cookie(key="session_token", secure=True, value=unic)
        fake_bd[username]["session_token"] = unic
        return {"Success": "good"}, {"your session_token": unic}


@app.put("/user")
def get_user(session_token=Cookie(), username: str = username_form):
    if not fake_bd[username]["session_token"] == session_token:
        raise HTTPException(status_code=401, detail={"message": "Unauthorized"})
    else:
        user = fake_bd[username]
        print(type(session_token))
        return User(**user), fake_bd[username]["session_token"], session_token


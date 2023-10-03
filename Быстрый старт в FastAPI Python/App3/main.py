from fastapi import FastAPI, Response, Depends
from fastapi import Form
from typing_extensions import Annotated
import random, httpx

app = FastAPI()

fake_bd = {
    "Igor": {
        "name": "Igor",
        "password": "abc123"
    }
}


def authenticate(bd, username: str, password: str):
    if username in bd:
        if bd[username]["password"] == password:
            return True


def gener_value():
    return str(random.random())


@app.get("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()], response: Response,
          unic: Annotated[str, Depends(gener_value)]):
    if authenticate(fake_bd, username, password):
        response.set_cookie(key="session_token", secure=True, value=unic)
        return {"a": "good"}


url = "http://127.0.0.1:8000/login"
params = {"username": "Igor", "password": "abc123"}
response = httpx.get(url, params=params)
print(response.status_code)
print(response.json())
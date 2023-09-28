from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import User, User2

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/html")
def root():
    with open("index.html", "r", encoding="utf-8") as a:
        b = a.read()

    return HTMLResponse(content=b)


@app.post("/calculate")
def func(num1: int, num2: int):
    return {"result": num1 + num2}


@app.get("/users", response_model=User)
def show():
    my_user: User = User(id=1, name="haha")
    return my_user


@app.post("/user")
def adult(user: User2):
    if int(user.age) >= 18:
        user.is_adult = True
    else:
        user.is_adult = False
    return user

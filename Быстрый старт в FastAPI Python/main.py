from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import User, User2, Feedback, UserCreate

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


fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

feds =[]


@app.post("/feedback")
def feeds(fed: Feedback):
    feds.append(fed.message)
    print(feds)
    return {"response": f"Feedback received. Thank you, {fed.name}!",
            "feds": f"{feds}"}


@app.post("/create_user", response_model = UserCreate)
def create(user: UserCreate):
    return user
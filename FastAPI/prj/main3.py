from fastapi import FastAPI
from models.models import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.get("/users")
def ho(user: User):
    return user

@app.post("/user")
def check_age(user: User):
    if user.age >= 18:
        return {"name": user.name,
                "age": user.age,
                "is_adult": "false"}
    else:
        return {"name": user.name,
                "age": user.age,
                "is_adult": "true"}




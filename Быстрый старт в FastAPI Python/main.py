from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}



@app.get("/html")
def root():
    with open("index.html", "r", encoding= "utf-8") as a:
        b = a.read()

    return HTMLResponse(content = b)

@app.post("/calculate")
def func(num1: int, num2: int):
    return {"result": num1+num2}
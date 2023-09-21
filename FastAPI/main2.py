from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def suum(num1: int, num2: int):
    result = num1+num2
    return {"result": result}

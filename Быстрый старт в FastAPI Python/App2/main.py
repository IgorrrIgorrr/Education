from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{product_id}")
def info(product_id: int):
    return product_id
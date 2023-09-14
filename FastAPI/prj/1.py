from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union


class Sample(BaseModel):
    product_id: int
    name: str
    category: str
    price: float


app = FastAPI()


@app.get("/product/{product_id}")
def prod_info(product_id: int):
    for i in sample_products:
        if i["product_id"] == product_id:
            return i
    else:
        return {"answer": "Not found"}

@app.get("/products/search")
def prod_search(keyword: str, category: Union[str, None] = None, limit: int = 10):
    a =[]
    for i in sample_products:
        if keyword in i["name"] and category == i["category"]:
            a.append(i)
    return a[:limit]


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]
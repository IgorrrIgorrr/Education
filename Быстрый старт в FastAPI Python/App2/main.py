from fastapi import FastAPI, Query
from typing import Union

app = FastAPI()


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


@app.get("/products/search")
def getprod(keyword: str, category: Union[str, None] = Query(default=None), limit: int = Query(default=10)):
    a =[]
    b = []
    for i in sample_products:
        if keyword in i["name"]:
            if category == i["category"]:
                b.append(i)
            a.append(i)
    if b:
        return b[:limit]
    else:
        return a[:limit]




@app.get("/product/{product_id}")
def info(product_id: int):
    a = []
    for i in sample_products:
        if product_id == i["product_id"]:
            a.append(i)
    return a




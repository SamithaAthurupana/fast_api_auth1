from dataclasses import dataclass
from fastapi import FastAPI,HTTPException
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: str
    name: str
    price: int

products: Dict[str, Product] = {}

@app.get("/")
def root():
    return "Products API"

@app.get("/products/")
def get_products():
    return list(products.values())

@app.get("/products/{product_id}")
def get_product(product_id: str):
    prd = Product(id="1", name="test", price=10)
    products[prd.id] = prd
    return products.get(product_id)

@app.post("/products")
def create_product(product:Product):
    products[product.id] = product
    return {"message": "successfully product added", "product": product}

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in products.keys():
        raise HTTPException(status_code=404, detail="product id not found to delete!")
    delete_prd = products.pop(product_id)

    return {"message": "successfully deleted", "product": delete_prd}


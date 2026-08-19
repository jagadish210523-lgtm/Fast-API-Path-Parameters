from fastapi import FastAPI
jaga = FastAPI()
@jaga.get("/products/{product_id}")
async def products(product_id):
    return f"Product ID is {product_id}"

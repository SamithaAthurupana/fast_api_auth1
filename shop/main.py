from fastapi import FastAPI
from routers.users_router import router as user_router
from routers.products_router import router as product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
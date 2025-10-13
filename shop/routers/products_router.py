from fastapi import APIRouter
from starlette import status

from shop.models import ProductResponse, ProductCreate
from shop.service import ProductService

router = APIRouter(prefix="/products", tags=["products"])

product_service = ProductService()


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(prod: ProductCreate):
    return product_service.create_product(prod)

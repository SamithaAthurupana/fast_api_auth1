from fastapi import APIRouter
from starlette import status

from shop.models import ProductResponse,ProductCreate
from shop.repository import InMemoryUserRepository
from shop.service import ProductService, UserService

router = APIRouter(prefix="/users", tags=["users"])

users_service = UserService(InMemoryUserRepository())


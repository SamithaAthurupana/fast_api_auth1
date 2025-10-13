from fastapi import APIRouter
from starlette import status
from shop.models import UserCreate, UserResponse
from shop.repository import InMemoryUserRepository
from shop.service import UserService

router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService(InMemoryUserRepository())


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    return user_service.create_user(user)

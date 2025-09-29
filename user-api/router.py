from datetime import datetime
from fastapi import APIRouter, status,HTTPException
from model import UserResponse, UserCreate
from service import UserService, UserServiceException

router = APIRouter(prefix = "/users", tags=["users"])
user_service = UserService()

@router.post("/", response_model = UserResponse, status_code = status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> UserResponse:
    # print(user)
    # return UserResponse(id=1, name="test", email="test@gmail.com",
    #                     role="user", created_at=datetime.now(), updated_at=datetime.now(), age=20)
    try:
        return user_service.create_user(user)
    except UserServiceException as e:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = str(e))

@router.get("/{user_id}")
def get_user(user_id: int) -> UserResponse:
    user = user_service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")

    return user


@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        user = user_service.delete_user(user_id)
        return {"message": f"Successfully deleted User - {user.email}"}
    except UserServiceException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
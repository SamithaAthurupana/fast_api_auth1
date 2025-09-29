from email.policy import default

from fastapi import APIRouter, status, HTTPException
from model import UserResponse, UserCreate
from service import UserService, UserServiceException

router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> UserResponse:

    try:
        return user_service.create_user(user)
    except UserServiceException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    user = user_service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate):
    try:
        updated_user = user_service.update_user(user_id, user)
        return {"message": "user updated successfully", "user": updated_user}
    except UserServiceException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        user = user_service.delete_user(user_id)
        return {"message": f"Successfully deleted User - {user.email}"}
    except UserServiceException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.patch("/{user_id}")
def patch_user(user_id: int, user: UserCreate):
    try:
        patch_user = user_service.patch_user(user_id, user)
        return {"message": "User Patched successfully", "patch_user": patch_user}
    except UserServiceException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = str(e))

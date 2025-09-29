from datetime import datetime
from http.client import HTTPException
from typing import Dict
from model import UserResponse, UserCreate, UserPatch


class UserServiceException(Exception):
    pass

class UserService:

    def __init__(self):
        self.users: Dict[int, UserResponse] = {}
        self.counter : int = 1

    def create_user(self, user: UserCreate) -> UserResponse:
        for user_obj in self.users.values():
            if user_obj.email == user.email:
                raise UserServiceException("Email already Exists!")
        user_resp = UserResponse(id = self.counter, email=user.email, age=user.age, role=user.role,
                                     name=user.name, created_at=datetime.now(), updated_at=datetime.now())

        self.users[self.counter] = user_resp
        self.counter += 1
        return user_resp

    def update_user(self, user_id:int, user: UserCreate) -> UserResponse:
        if user_id not in self.users.keys():
            raise UserServiceException("Invalid user id!")
        existing_user = self.users[user_id]

        self.users[user_id] = UserResponse(
            id = user_id,
            email=user.email,
            age=user.age,
            role=user.role,
            name=user.name,
            created_at=existing_user.created_at,
            updated_at=datetime.now()
        )
        return self.users[user_id]

    def get_user(self, user_id: int) -> UserResponse:
        return self.users.get(user_id)

    def delete_user(self,user_id: int) -> UserResponse:
        if user_id not in self.users.keys():
            raise UserServiceException("User ID not found")
        user = self.users.pop(user_id)
        return user

    def patch_user(self, user_id:int, user:UserPatch):
        if user_id not in self.users.keys():
            raise UserServiceException("User ID not found for patching")

        existing_user = self.users[user_id]
        updated_data = user.model_dump(exclude_unset=True) # Creating a dictionary using the UserPatch instance
        updated_user = existing_user.model_copy(update=updated_data) # Copying the UserResponse
        self.users[user_id] = updated_user                                  #

        return self.users[user_id]
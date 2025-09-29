from datetime import datetime
from typing import Dict
from model import UserResponse, UserCreate

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

    def get_user(self, user_id: int) -> UserResponse:
        return self.users.get(user_id)

    def delete_user(self,user_id: int) -> UserResponse:
        if user_id not in self.users.keys():
            raise UserServiceException("User ID not found")
        user = self.users.pop(user_id)
        return user
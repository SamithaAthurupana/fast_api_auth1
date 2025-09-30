from datetime import datetime
from http.client import HTTPException
from typing import Dict, List
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

    def patch_user(self, user_id: int, user: UserPatch) -> UserResponse:
        if user_id not in self.users:
            raise UserServiceException("User ID not found for patching")

        existing_user: UserResponse = self.users[user_id]

        # If email is being patched, check uniqueness against other users
        patch_data = user.model_dump(exclude_unset=True)
        new_email = patch_data.get("email")
        if new_email and new_email != existing_user.email:
            for uid, u in self.users.items():
                if uid != user_id and u.email == new_email:
                    raise UserServiceException("Email already Exists!")

        # Create updated user copy and ensure updated_at is changed
        updated_user = existing_user.model_copy(update=patch_data)
        updated_user.updated_at = datetime.now()

        self.users[user_id] = updated_user
        return updated_user

    def get_all_users(self, offset: int = 0, limit: int = 10) -> List[UserResponse]:
        # sanitize inputs
        if offset < 0:
            raise UserServiceException("Offset must be >= 0")
        if limit <= 0:
            raise UserServiceException("Limit must be > 0")
        max_limit = 100
        if limit > max_limit:
            limit = max_limit

        users_list = list(self.users.values())  # preserves insertion order (py3.7+)
        return users_list[offset: offset + limit]

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional

from shop.models import UserPatch, UserCreate, UserResponse


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate) -> UserResponse:
        pass

    @abstractmethod
    def update_user(self, user: UserCreate, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def patch_user(self, user: UserPatch, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def get_by_username(self, name: str) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass


class UserServiceException(Exception):
    pass


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[int, UserResponse] = {}
        self.count: int = 1

    def create_user(self, user: UserCreate) -> UserResponse:
        user_obj = UserResponse(
            id=self.count,
            name=user.name,
            email=user.email,
            age=user.age,
            role=user.role,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.users[self.count] = user_obj
        self.count += 1
        return user_obj

    def update_user(self, user: UserCreate, user_id: int) -> UserResponse:
        if user_id not in self.users:
            raise UserServiceException("Invalid User Id")

        existing_user = self.users[user_id]
        updated_user = UserResponse(
            id=user_id,
            name=user.name,
            email=user.email,
            age=user.age,
            role=user.role,
            created_at=existing_user.created_at,
            updated_at=datetime.now()
        )
        self.users[user_id] = updated_user
        return updated_user

    def patch_user(self, user: UserPatch, user_id: int) -> UserResponse:
        if user_id not in self.users:
            raise UserServiceException("User ID not found for patching")

        existing_user = self.users[user_id]
        updated_data = user.model_dump(exclude_unset=True)
        updated_user = existing_user.model_copy(update=updated_data)
        self.users[user_id] = updated_user
        return updated_user

    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        return self.users.get(user_id)

    def get_by_username(self, name: str) -> Optional[UserResponse]:
        return next((u for u in self.users.values() if u.name == name), None)

    def get_by_email(self, email: str) -> Optional[UserResponse]:
        return next((u for u in self.users.values() if u.email == email), None)

    def delete(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional

from main import update_student
from models import UserResponse
from shop.models import UserPatch, UserCreate



class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user:UserCreate) -> UserResponse:
        pass

    @abstractmethod
    def update_user(self, user: UserCreate , user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def patch_user(self, user: UserCreate , user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def get_by_id(self, user_id:int) -> UserResponse:
        pass

    @abstractmethod
    def get_by_username(self, name:str) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def get_by_email(self, email:str) -> UserResponse:
        pass

    @abstractmethod
    def delete(self, user_id:int) -> bool:
        pass


class UserServiceException(Exception):
    pass


class InMemoryUserRepository(UserRepository):


    def init(self):
        self.users: Dict[int, UserResponse] = {}
        self.count: int = 0

    def create_user(self, user:UserCreate) -> UserResponse:

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

        if user_id not in self.users.keys():
            raise UserServiceException("Invalid User Id")

        exiting_user = self.users[user_id]

        self.users[user_id] = UserResponse(
            id=user_id,
            name=user.name,
            email=user.email,
            age=user.age,
            role=user.role,
            created_at=exiting_user.created_at,
            updated_at=datetime.datetime.now()
        )

        updated_user = self.users[user_id]

        return updated_user

    def patch_user(self, user: UserPatch, user_id: int) -> UserResponse:

        if user_id not in self.users.keys():
            raise UserServiceException("User ID not found for patching")

        exiting_user = self.users[user_id]

        # Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
        # exclude_unset: Whether to exclude fields that have not been explicitly set.
        # mekedi wenne unset kpu ewa exclude etkot one dewal witry dictionary ekakat add wenne
        # me model dump eken wenne apita update wenna one dewal tika witrk update krnwa
        updated_data = user.model_dump(exclude_unset=True) #methanadi dictoinary ekak hadagaththe model copy ekata danna one nisa update wenna opne dewal tika witrk

        updated_user = exiting_user.model_copy(update=updated_data) # methanadi userge data update ekak wenwa

        self.users[user_id] = updated_user # mekedi adala user_id ekt update krnwa

        return self.users[user_id]

    def get_by_id(self, user_id: int) -> UserResponse:

        return self.users.get(user_id)

    def get_by_username(self, name: str) -> Optional[UserResponse]:

        for user_line in self.users.values():

            if user_line.name == name:
                return user_line

        return None

    def get_by_email(self, email: str) -> Optional[UserResponse]:

    # mekedi krlathiyenne email eka ganna kalin user {} eka access krla values wlt gihilla ethanin mail eka access krnwa

        for user_line in self.users.values():

            if user_line.email == email:
                return user_line

        return None

    def delete(self, user_id: int) -> bool:
        pass
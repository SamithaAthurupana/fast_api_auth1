from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from shop.models import UserCreate, ProductResponse, ProductCreate
from shop.repository import UserRepository, UserServiceException


@dataclass
class UserService:

    user_repository: UserRepository

    def create_user(self, user:UserCreate):

        if self.user_repository.get_by_email(user.email) is not None:
            raise UserServiceException("Email already exists")

        self.user_repository.create_user(user)


class ProductService:
    def __init__(self):
        self.products: Dict[int, ProductResponse] = {}
        self.count: int = 1

    def create_product(self, prod: ProductCreate) -> ProductResponse:
        prod = ProductResponse(
            id=self.count,
            name=prod.name,
            description=prod.description,
            price=prod.price,
            category=prod.category,
            created_at=datetime.now(),
            updated_at=datetime.now()

        )

        self.products[self.count] = prod
        self.count += 1
        return prod

    def get_all(self) -> List[ProductResponse]:
        return list(self.products.values())

from dataclasses import field
from datetime import datetime
from itertools import product
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: int = Field(..., ge=0, le=100)
    role: str

    @field_validator('email')
    def validate_email(cls, v: str) -> str:
        return v.lower()

    # write a custom validator logic to validator age,
    # if age less than 13 raise valueError saying age must be grater than 13
    # if age grater than 13 return the age

    @field_validator('age')
    def validate_age(cls, v: int) -> int:
        if v < 13:
            raise ValueError ("Age must be grater than 13")
        return v


user = UserCreate(name = "test", email = "test@gmail.com", age = 18, role = "admin")
print(user)

class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[str] = Field(None,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: Optional[int] = Field(None, ge=0, le=100)
    role: Optional[str] = None

    @field_validator('email')
    def validate_email(cls, v: str) -> str:
        return v.lower()

class UserResponse(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime



class ProductCreate(BaseModel):
    name:str = Field(..., min_length=2, max_length=100)
    description: str =Field(..., min_length=4, max_length=300)
    price: float = Field(..., ge=0)
    category: str = Field(..., min_length=2, max_length=100)
    tags: List[str] = Field(default_factory=list)

    @field_validator('tags')
    def validate_tags(cls, v:List[str]) -> List[str]:
        if len(v) > 10:
            raise ValueError("you can't add 10 more tags")
        return v

class ProductResponse(ProductCreate):
    id : int
    created_at: datetime
    updated_at: datetime


from dataclasses import field
from datetime import datetime
from itertools import product
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, field_validator, EmailStr


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=0, le=100)
    role: str

    @field_validator('email')
    def validate_email(cls, v: str) -> str:
        return v.lower()

    @field_validator('age')
    def validate_age(cls, v: int) -> int:
        if v < 13:
            raise ValueError("Age must be greater than 13")
        return v


class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[str] = Field(None)
    age: Optional[int] = Field(None, ge=0, le=100)
    role: Optional[str] = None

    @field_validator('email')
    def validate_email(cls, v: str) -> str:
        return v.lower() if v else v


class UserResponse(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=4, max_length=300)
    price: float = Field(..., ge=0)
    category: str = Field(..., min_length=2, max_length=100)
    tags: List[str] = Field(default_factory=list)

    @field_validator('tags')
    def validate_tags(cls, v: List[str]) -> List[str]:
        if len(v) > 10:
            raise ValueError("You can't add more than 10 tags")
        return v


class ProductResponse(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime
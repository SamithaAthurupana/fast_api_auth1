from dataclasses import field
from datetime import datetime
from typing import Optional
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
    created_at: str
    updated_at: str
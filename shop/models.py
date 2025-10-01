from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: int = Field(..., ge=0, le=100)
    role: str

class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[str] = Field(None,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: Optional[int] = Field(None, ge=0, le=100)
    role: Optional[str] = None

class UserResponse(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime
from datetime import datetime

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    role: str

class UserResponse(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime
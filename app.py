from datetime import date
from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_date: Optional[date] = None
    friends: list[int] = []
    email: str

    @field_validator('email')
    def validate_email(cls, v):
        if v <= 0:
            raise ValueError('ID must be a postive integer')
        return v
    
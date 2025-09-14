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

try:
    user1 = User(id=123, email="jane.doe@example.com", signup_date="2024-01-01")
    print("User 1 is valid:")
    print(user1.model_dump_json(indent=2))
    print("-" * 20)
    user2 = User(id=456)
    print("This wont be printed")

except ValidationError as e:
    print("Validation Error Caught!")
    print(e)
    print("-" * 20)

try:
    user3 = User(id=-789, email="invalid.id@example.com")
    print("This wont be printed")

except ValidationError as e:
    print("Validation Error for invalid ID:")
    print(e)

print("\nAccessing data from user1:")
print(f"Name: {user1.name}")
print(f"Email: {user1.email}")
print(f"Sign-up Date: {user1.signup_date}")
print(f"friends: {user1.friends}")


from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str   

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        if not re.match(pattern, password):
            raise ValueError(
                "Password must be at least 8 characters long and include letters, numbers, and special characters."
            )
        return password


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class SearchTerm(BaseModel):
    term: str

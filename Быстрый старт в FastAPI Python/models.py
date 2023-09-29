from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    name: str
    id: int

class User2(BaseModel):
    name: str
    age: int
    is_adult: bool = False

class Feedback(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0)
    is_subscribed: bool = None

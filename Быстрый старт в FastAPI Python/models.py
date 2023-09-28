from pydantic import BaseModel


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

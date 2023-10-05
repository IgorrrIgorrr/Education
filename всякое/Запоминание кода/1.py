from typing_extensions import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Union

fake_db = {
    "Mike": {
        "username": "Mike",
        "full_name": "MikeTyson",
        "emai": "ha@ya.com",
        "hashed_password": "fakefake",
        "disabled": False,
    }
}

app = FastAPI()


def fake_hashed_password(password: str):
    return "fakepassword" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str



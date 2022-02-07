from typing import List, Optional
from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class User(BaseModel):
    username: str
    email: Optional[str] = None
    is_active: bool

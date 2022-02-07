import typing
import uuid
import warnings
import ormar
from app.db import BaseMeta
import pydantic

class User:
    id : typing.Optional[int] = ormar.Integer(primary_key=True)
    hashed_password: str = ormar.String(nullable=True, max_length=255)

class UserModel(ormar.Model, User):
    username :str = ormar.String(nullable=False, unique=True, max_length=15)
    email : str = ormar.String(nullable=False, max_length=255)
    role :str = ormar.String(nullable=False, default="user", max_length=30)
    is_active: bool = ormar.Boolean(nullable=False, default=False)
    confirmation: uuid = ormar.UUID(nullable=True)
    
    class Meta(BaseMeta):
        tablename = "users"


ResponseUser = UserModel.get_pydantic(exclude={'hashed_password', 'confirmation'})
UserInPy = UserModel.get_pydantic(include={'username','email'})

class UserIn(UserInPy):
    password : str

class test(ResponseUser):
    full_name : typing.Optional[str]
        
    @pydantic.validator('full_name', always=True)
    def fulname(cls,v ,values) -> str:
        if values['role'] == 'user':
            return 'Siemka'
        else:
            return 'Ullaaa'

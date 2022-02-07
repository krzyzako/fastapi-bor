from datetime import timedelta
import datetime
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jose import JWTError, jwt
from typing import List, Optional
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError
from app.models.users import UserModel
from app.config.settings import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/auth/token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)
setting = get_settings()


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class User(BaseModel):
    username: str
    email: Optional[str] = None


class Auth:
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

    async def get_user(username: str):
        user = await UserModel.objects.filter(username=username).get_or_none()
        return user.dict()

    async def authenticate_user(username: str, password: str):
        user = await Auth.get_user(username)
        if not user:
            return False
        if not Auth.verify_password(password, user["hashed_password"]):
            return False
        return user

    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.TOKEN_ALGORITHM)
        return encoded_jwt

    async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = f"Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, setting.SECRET_KEY, algorithms=[setting.TOKEN_ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_scopes = payload.get("scopes", [])
            token_data = TokenData(scopes=token_scopes, username=username)
        except (JWTError, ValidationError):
            raise credentials_exception
        user = Auth.get_user(username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user

    async def get_current_active_user(current_user: User = Security(get_current_user, scopes=["me"])):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

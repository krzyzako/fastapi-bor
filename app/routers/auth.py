import socket
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status, APIRouter


# from app.service.auth import Auth
# from app.service import auth
# from app.service.mailer import send_email_async
from app.config.settings import get_settings
from app.models import users
from jose import jwt
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

auth_router = APIRouter(
    prefix="/api/auth",
    tags=["Autoryzacja"],
)


@auth_router.post("/login/")
async def tes(login_data: OAuth2PasswordRequestForm = Depends()):
    if login_data.username == "krzyzak":
        return {"access_token": "access_token", "token_type": "bearer"}
    else:
        return {}


@auth_router.post("/me")
async def tes(login_data: OAuth2PasswordRequestForm = Depends()):
    print(login_data)
    return {"user": login_data}


# @auth_router.get("/login")
# async def login(login_data: OAuth2PasswordRequestForm = Depends()):
#     user: users.UserModel = await Auth.get_user(login_data.username)
#     if not Auth.veryfity_password(login_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Wrong password",
#         )
#     if not user.is_active:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail=f"{user.username.capitalize()} account is not active, chech your email",
#         )
#     access_token = Auth.get_token({"username": user.username}, 28800)

#     return {"access_token": access_token, "token_type": "bearer"}


# @auth_router.get("/me", response_model=users.test)
# async def show_me(
#     login_data: users.UserModel = Depends(auth.get_current_user),
# ):
#     user = await users.UserModel.objects.get_or_none(username=login_data.username)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User not exists",
#         )
#     if not user.is_active:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail=f"{user.username.capitalize()} account is not active, chech your email",
#         )
#     us = users.ResponseUser(**user.dict(exclude_unset=True))
#     return us


# @auth_router.post("/logout")
# async def login():
#     return {"msg": "ok"}


# @auth_router.post("/register")
# async def register(form_data: users.UserIn):
#     if await users.UserModel.objects.get_or_none(email=form_data.email) is not None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Podany adres email istnieje",
#         )
#     if await users.UserModel.objects.get_or_none(username=form_data.username) is not None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User already exists",
#         )
#     domena = form_data.email.split("@")
#     print(domena[1])
#     # if domena[1] != "bormech.pl" :
#     #     raise HTTPException(
#     #         status_code=status.HTTP_400_BAD_REQUEST,
#     #         detail="Tylko dla adresów bormech.pl"
#     #     )

#     user = await users.UserModel(
#         username=form_data.username,
#         email=form_data.email,
#         hashed_password=Auth.get_password_hash(form_data.password),
#     ).save()
#     await user.load()
#     confirmation = Auth.get_confirmation_token(user.id)
#     user.confirmation = confirmation["jti"]
#     "u".capitalize()
#     print(list(form_data.email))
#     await send_email_async(
#         subject="Aktywacja konta",
#         email_to=form_data.email,
#         body={
#             "title": f"Aktywacja konta {form_data.username.capitalize() }",
#             "name": f"Witaj {form_data.username.capitalize()}",
#             "token": confirmation["token"],
#             "host": socket.gethostbyname(socket.gethostname()),
#         },
#     )
#     await user.update()


# @auth_router.get("/aktywacja/{token}")
# async def verify(token: str):
#     invalid_token_error = HTTPException(status_code=400, detail="Invalid token")
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.TOKEN_ALGORITHM)
#     except jwt.JWTError:
#         raise HTTPException(status_code=403, detail="Token has expired")
#     if payload["scope"] != "registration":
#         raise invalid_token_error
#     user = await users.UserModel.objects.get_or_none(id=int(payload["sub"]))
#     if not user or str(user.confirmation) != payload["jti"]:
#         raise invalid_token_error
#     if user.is_active:
#         raise HTTPException(status_code=403, detail="User already activated")
#     user.confirmation = None
#     user.is_active = True
#     await user.update()
#     await user.load()
#     return user.dict(exclude={"hashed_password"})

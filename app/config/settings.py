from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLITE_FILE_NAME: str
    SECRET_KEY: str
    APP_NAME = 'My App'
    VERSION: str
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    TOKEN_ALGORITHM = 'HS256'
    SMTP_SERVER: Optional[str]
    MAIL_SENDER = 'lukasz.l@bormech.pl'
    API_PREFIX = '/api'
    HOST = 'localhost'
    PORT = 8000
    BASE_URL = '{}:{}'.format(HOST, str(PORT))
    MODELS = [
        'app.models.users',
        'app.models.approval',
    ]
    ADMIN_NAME: str = "admin"
    ADMIN_PASSWORD: str = "bormech1234"
    ADMIN_LAST_NAME: str = "Lindstedt"
    ADMIN_FIRST_NAME: str = "Łukasz"

    MAIL_USERNAME: str = "api.bormech@gmail.com"
    MAIL_PASSWORD: str = "fagbharqtetprsho"
    MAIL_FROM: str = "api.bormech@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "BormAdmin"

    class Config:
        env_file = '.env'
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings()

import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings
import secrets
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    PROJECT_NAME: str = "Code Writer"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY")
    TEXT_MODEL: str = os.environ.get("TEXT_MODEL")
    IMAGE_MODEL: str = os.environ.get("IMAGE_MODEL")
    IMAGE_SIZE: str = os.environ.get("IMAGE_SIZE")
    TEMPERATURE: float = os.environ.get("TEMPERATURE")
    NUMBER_IMAGE: int = os.environ.get("NUMBER_IMAGE")
    IMAGE_QUALITY: str = os.environ.get("IMAGE_QUALITY")
    

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()

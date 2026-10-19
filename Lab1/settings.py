# settings.py
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    api_key: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str):
        allowed = ("dev", "test", "prod")
        if value not in allowed:
            raise ValueError("ENVIRONMENT must be one of: dev, test, prod")
        return value

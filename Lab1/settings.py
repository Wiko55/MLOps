# settings.py
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.test", env_file_encoding="utf-8")

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

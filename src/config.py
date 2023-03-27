from pydantic import BaseSettings


class Config(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


config = Config()

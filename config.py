import os

from pydantic import PositiveInt
from pydantic_settings import BaseSettings


class MongoSettings(BaseSettings):

    username: str = os.getenv("MONGO_USERNAME")  # type: ignore
    password: str = os.getenv("MONGO_PASSWORD")  # type: ignore
    host: str = os.getenv("MONGO_HOST")
    port: PositiveInt = os.getenv("MONGO_PORT")
    database_name: str = os.getenv("MONGO_DATABASE_NAME")
    url: str = f"mongodb://{username}:{password}@{host}:{port}/"


class Settings(BaseSettings):
    mongodb: MongoSettings = MongoSettings()


settings = Settings()

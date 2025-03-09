from typing import Literal

from motor.motor_asyncio import AsyncIOMotorDatabase

from repositories.repositories import Repository


class MongoDBHelper:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    def repository_factory(
        self, repository_name: Literal["audiences", "users", "reservations"]
    ) -> Repository:
        collection = self.__database[repository_name]
        return Repository(collection)

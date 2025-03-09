from motor.motor_asyncio import AsyncIOMotorClient

from .db_helper import MongoDBHelper
from ..config import settings

client = AsyncIOMotorClient(settings.mongodb.url)
booking_bot_db = client[settings.mongodb.database_name]
mongo_db_helper = MongoDBHelper(booking_bot_db)

audiencies_repository = mongo_db_helper.repository_factory("audiences")
reservations_repository = mongo_db_helper.repository_factory("reservations")
users_repository = mongo_db_helper.repository_factory("users")

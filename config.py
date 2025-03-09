from pymongo import MongoClient


class Config:
    MONGO_URI = "mongodb://username:password@localhost:27017/"
    DATABASE_NAME = "bookingservice"

config = Config()

client = MongoClient(config.MONGO_URI)
db = client[config.DATABASE_NAME]
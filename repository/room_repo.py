from pymongo.collection import Collection
from config import db
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure  # Исправляем импорт

class RoomRepository:
    def __init__(self):
        self.rooms_collection: Collection = db.rooms
        self.counters_collection: Collection = db.counters

    def get_next_room_number(self):
        try:
            counter = self.counters_collection.find_one_and_update(
                {"_id": "room_number"},
                {"$inc": {"seq": 1}},
                upsert=True,
                return_document=True
            )
            return counter["seq"] + 407 if counter["seq"] else 408
        except ConnectionFailure as e:  # Исправляем на ConnectionFailure
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def add_room(self, room_data):
        try:
            result = self.rooms_collection.insert_one(room_data.dict())
            return str(result.inserted_id)
        except ConnectionFailure as e:  # Исправляем на ConnectionFailure
            raise Exception(f"Failed to add room: {e}")

    def get_all_rooms(self):
        try:
            return list(self.rooms_collection.find())
        except ConnectionFailure as e:  # Исправляем на ConnectionFailure
            raise Exception(f"Failed to fetch rooms: {e}")

    def get_room_by_id(self, room_id: str):
        try:
            room = self.rooms_collection.find_one({"_id": ObjectId(room_id)})
            if room:
                room["_id"] = str(room["_id"])
                return room
            return None
        except ConnectionFailure as e:  # Исправляем на ConnectionFailure
            raise Exception(f"Failed to fetch room by ID: {e}")

room_repo = RoomRepository()
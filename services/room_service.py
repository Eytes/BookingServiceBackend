from repository.room_repo import room_repo
from schemas.room import RoomCreate, RoomResponse
from fastapi import HTTPException

class RoomService:
    def create_room(self, room_data: RoomCreate):
        try:
            room_number = room_repo.get_next_room_number()
            room_data_dict = room_data.dict()
            room_data_dict["title"] = f"кабинет {room_number}"
            room_id = room_repo.add_room(RoomCreate(**room_data_dict))
            return room_id
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def list_rooms(self):
        try:
            rooms = room_repo.get_all_rooms()
            return [RoomResponse(**room, id=str(room["_id"])) for room in rooms]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_room(self, room_id: str):
        try:
            room = room_repo.get_room_by_id(room_id)
            if room:
                return RoomResponse(**room, id=str(room["_id"]))
            raise HTTPException(status_code=404, detail="Room not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

room_service = RoomService()
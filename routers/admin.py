from fastapi import APIRouter, HTTPException
from schemas.room import RoomCreate, RoomResponse
from services.room_service import room_service
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/rooms", response_model=RoomResponse, status_code=201)
async def create_room(room: RoomCreate):
    """Create a new room with an auto-generated title in the format 'кабинет <id>'.
    Args:
        room (RoomCreate): Room details (booking, available_times).
    Returns:
        RoomResponse: Created room with ID and auto-generated title.
    """
    try:
        room_id = room_service.create_room(room)
        room_data = room_service.get_room(room_id)
        if room_data:
            return room_data
        raise HTTPException(status_code=500, detail="Failed to retrieve created room")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/rooms", response_model=List[RoomResponse])
async def get_rooms():
    """Get all rooms.
    Returns:
        List[RoomResponse]: List of all rooms.
    """
    rooms = room_service.list_rooms()
    if not rooms:
        raise HTTPException(status_code=404, detail="No rooms found")
    return rooms

@router.get("/rooms/{room_id}", response_model=RoomResponse)
async def get_room(room_id: str):
    """Get a room by ID.
    Args:
        room_id (str): The ID of the room.
    Returns:
        RoomResponse: Room details.
    """
    room = room_service.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
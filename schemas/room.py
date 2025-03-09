from pydantic import BaseModel
from typing import List, Optional
from pydantic import Field

class RoomTimeSlot(BaseModel):
    time: str = Field(..., example="9:00")
    busy: bool = Field(default=False, example=False)

class RoomCreate(BaseModel):
    # title убираем, так как он будет генерироваться автоматически
    booking: dict = Field(default={}, example={})
    available_times: List[RoomTimeSlot] = Field(..., example=[
        {"time": "9:00", "busy": False},
        {"time": "9:30", "busy": False}
    ])

class RoomResponse(BaseModel):
    id: str
    title: str
    booking: dict
    available_times: List[RoomTimeSlot]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "title": "кабинет 408",
                "booking": {},
                "available_times": [
                    {"time": "9:00", "busy": False},
                    {"time": "9:30", "busy": False}
                ]
            }
        }
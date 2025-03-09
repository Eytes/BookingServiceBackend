from backend.repositories import (
    audiencies_repository,
    reservations_repository,
    users_repository,
)
from .audience import AudienceService
from .reservation import ReservationService
from .user import UserService

audience_service = AudienceService(audiencies_repository)
reservation_service = ReservationService(reservations_repository)
user_service = UserService(users_repository)

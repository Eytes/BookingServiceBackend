from ..base_types import ItemId
from ..catcher_of_errors import ResultNotFoundError
from ..repositories import reservations_repository
from ..schemas.reservation import (
    CreateReservationSchema,
    UpdateReservationSchema,
    ReservationSchema,
)


class ReservationService:
    """
    Сервис для работы с бронированиями.
    """

    async def create(
        self, reservation: CreateReservationSchema
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Создает новое бронирование."""
        res = reservations_repository.create(reservation)
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def update(
        self, reservation_id: ItemId, new_data: UpdateReservationSchema
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Обновляет существующее бронирование."""
        res = reservations_repository.update(reservation_id, new_data)
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def get_by_id(
        self, objects_id: list
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Возвращает список бронирований."""
        res = reservations_repository.get(objects_id)
        if res == ItemId:
            return res
        return ResultNotFoundError

    # async def get_by_id(self, reservation_id: ItemId) -> BaseModel  :
    #     """Возвращает бронирование по его ID."""
    #     return result_not_found(
    #         await    reservation_repository.get_one(reservation_id),
    #         reservation_not_found,
    #     )
    # async def get_users_by_reservations_id(
    #     self, reservations_id: ItemId
    # ) -> list[UserSchema]:
    #     """Возвращает пользователя, связанного с указанным бронированием."""
    #     return await UserService.get(reservation_repository.get(reservations_id)[0])

    async def get_by_start_time(
        self, reservation_start_time: ReservationSchema.since_datetime
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Возвращает список бронирований, начинающихся в указанное время."""
        res = reservations_repository.get(reservation_start_time, "since_time")
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def get_by_end_time(
        self, reservation_end_time: ReservationSchema.until_datetime
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Возвращает список бронирований, заканчивающихся в указанное время."""
        res = reservations_repository.get(reservation_end_time, "until_time")
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def delete_by_id(
        self, reservation_id: ItemId
    ) -> ReservationSchema | type[ResultNotFoundError]:
        """Удаляет бронирование по его ID."""
        res = reservations_repository.delete(reservation_id)
        if res == ItemId:
            return res
        return ResultNotFoundError

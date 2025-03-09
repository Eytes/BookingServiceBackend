from ..base_types import ItemId
from ..catcher_of_errors import ResultNotFoundError
from ..repositories import audience_repository
from ..schemas.user import (
    CreateUserSchema,
    UserSchema,
    UpdateUserSchema,
)


class UserService:
    """
    Сервис для работы с пользователями.
    """

    async def create(
        self, user: CreateUserSchema
    ) -> ItemId | type[ResultNotFoundError]:
        """Создает нового пользователя."""
        res = audience_repository.create(user.model_dump())
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def update(
        self, user_id: ItemId, new_data: UpdateUserSchema
    ) -> UserSchema | type[ResultNotFoundError]:
        """Обновляет существующую аудиторию."""
        res = UserSchema.model_validate(
            await audience_repository.update(user_id, new_data)
        )
        if res == ItemId:
            return res
        return ResultNotFoundError

    async def get(
        self, objects_id: list[UserSchema.id]
    ) -> list[UserSchema] | type[ResultNotFoundError]:
        """Возвращает список всех пользователей."""
        res = audience_repository.get("id", objects_id)
        if res == ItemId:
            return res
        return ResultNotFoundError

    # async def get_by_id(self, user_id: ItemId) -> BaseModel  :
    #     """Возвращает пользователя по его ID."""
    #     return result_not_found(
    #         await  audience_repository.get_one(user_id),
    #         user_not_found,
    #     )

    async def delete_by_id(
        self, user_id: ItemId
    ) -> UserSchema | type[ResultNotFoundError]:
        """Удаляет пользователя по его ID."""
        res = audience_repository.delete(user_id)
        if res == ItemId:
            return res
        return ResultNotFoundError

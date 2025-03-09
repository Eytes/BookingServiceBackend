from ..base_types import ItemId
from ..catcher_of_errors import ResultNotFoundError
from ..repositories.repositories import Repository
from ..schemas.audience import (
    AudienceSchema,
    UpdateAudienceSchema,
    AudienceBaseSchema,
)


class AudienceService:
    """
    Сервис для работы с аудиториями.
    """

    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    async def create(self, audience: AudienceBaseSchema) -> ItemId:
        """Создает новую аудиторию."""
        res = await self.repository.create(audience.model_dump())
        if res:
            return res
        raise ResultNotFoundError

    async def update(
        self, audience_id: ItemId, new_data: UpdateAudienceSchema
    ) -> AudienceSchema:
        """Обновляет существующую аудиторию."""
        res = AudienceSchema(
            **(await self.repository.update(audience_id, new_data.model_dump()))
        )
        if res:
            return res
        raise ResultNotFoundError

    async def get(
        self,
        field_name: str | None = None,
        values: list | None = None,
        limit: int = 10,
        skip: int = 0,
    ) -> list[AudienceSchema]:
        if values and field_name:
            res = list(
                map(
                    AudienceSchema.model_validate,
                    await self.repository.get(field_name, values, limit, skip),
                )
            )
        else:
            res = list(
                map(
                    AudienceSchema.model_validate,
                    await self.repository.get(limit=limit, skip=skip),
                )
            )
        if res:
            return res
        raise ResultNotFoundError

    async def delete_by_id(self, audience_id: ItemId) -> bool:
        """Удаляет аудиторию по ее ID."""
        await self.get("id", [audience_id])
        return await self.repository.delete(audience_id)

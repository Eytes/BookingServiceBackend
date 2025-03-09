from api.api import API
from base_types import ItemId
from schemas.audience import (
    AudienceBaseSchema,
    AudienceSchema,
    UpdateAudienceSchema,
)


class AudienceApi(API):
    router = super().create_api_router("audience", ["Audiences"])
    """
    API для работы с аудиториями.
    """

    @router.post("/audience/post")
    async def create(self, audience: AudienceBaseSchema) -> ItemId:
        return await self.__service.create(audience)

    @router.put("/audience/put")
    async def update(
        self, audience_id: ItemId, new_data: UpdateAudienceSchema
    ) -> AudienceSchema:
        return await self.__service.update(audience_id, new_data)

    @router.get("/audience/get/all")
    async def get_all(self) -> list[AudienceSchema]:
        """Возвращает список всех аудиторий."""
        return await self.__service.get_all()

    @router.get("/audience/get/by_id")
    async def get_by_id(self, audiences_id: ItemId) -> AudienceSchema:
        """Возвращает аудиторию по ее ID."""
        return await self.__service.get_by_id(audiences_id)

    @router.get("/audience/get")
    async def get_by_capacity(
        self, audience_capacity: list[AudienceSchema.capacity]
    ) -> AudienceSchema:
        """Возвращает список аудиторий с указанной вместимостью."""
        return await self.__service.get_by_capacity(audience_capacity)

    @router.delete("/audience/delete")
    async def delete_by_id(self, audience_id: ItemId) -> AudienceSchema:
        """Удаляет аудиторию по ее ID."""
        return await self.__service.delete_by_id(audience_id)

from motor.motor_asyncio import AsyncIOMotorCollection


class Repository:

    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection

    async def create(self, data: dict) -> str:
        """Создает новую запись в базе данных."""
        return str((await self.collection.insert_one(data)).inserted_id)

    async def update(self, object_id: str, new_data: dict) -> dict:
        """Обновляет существующую запись в базе данных."""
        return await self.collection.find_one_and_update(
            {"id": object_id},
            {"$set": new_data},
        )

    async def delete(self, object_id: str) -> bool:
        """Удаляет запись из базы данных по id."""
        return bool((await self.collection.delete_one({"id": object_id})).deleted_count)

    async def get(
        self,
        field_name: str | None = None,
        values: list | None = None,
        limit: int = 10,
        skip: int = 0,
    ) -> list[dict | None]:
        """Возвращает список записей из базы данных."""
        return (
            [
                item
                async for item in self.collection.find({field_name: {"$in": values}})
                .skip(skip)
                .limit(limit)
            ]
            if values
            else [item async for item in self.collection.find().skip(skip).limit(limit)]
        )

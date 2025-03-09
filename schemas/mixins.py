from uuid import uuid4

from pydantic import BaseModel, Field

from ..base_types import ItemId


class MixinId(BaseModel):
    id: ItemId = Field(default_factory=lambda: uuid4().hex)

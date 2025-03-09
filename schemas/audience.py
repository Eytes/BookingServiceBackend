from pydantic import BaseModel

from .mixins import MixinId


class AudienceBaseSchema(BaseModel):
    capacity: int
    description: str


class AudienceSchema(AudienceBaseSchema, MixinId):
    pass


class CreateAudienceSchema(AudienceSchema):
    pass


class UpdateAudienceSchema(AudienceBaseSchema):
    pass

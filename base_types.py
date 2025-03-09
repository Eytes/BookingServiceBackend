from typing import TypeAlias, Annotated
from uuid import UUID

ItemId: TypeAlias = Annotated[str, UUID.hex]

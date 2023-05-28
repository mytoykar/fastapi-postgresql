from typing import Optional

from pydantic import BaseModel


class Filters(BaseModel):
    character_id: Optional[int] = None
    name: Optional[str] = ""


class PaginationParams(BaseModel):
    skip: Optional[int] = 0
    limit: Optional[int] = 100
    filters: Optional[Filters] = None

    class Config:
        anystr_strip_whitespace = True


async def pagination_params(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    character_id: Optional[int] = None,
    name: Optional[str] = None,
):

    filters = Filters(
        character_id=character_id,
        name=name,
    )

    return PaginationParams(
        skip=skip,
        limit=limit,
        filters=filters,
    )

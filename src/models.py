from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class MatchExtra(BaseModel):
    name: str
    type: str
    params: list | None = None


class Match(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    trigger: str
    replace: str
    vars: list[MatchExtra] | None = None
    tags: list[str] | None = None

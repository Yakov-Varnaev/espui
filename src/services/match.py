from uuid import UUID
from src.exceptions import NotFound
from src.models import Match
from src.repo import MatchFileRepository


class BaseService:
    def __init__(self, db:MatchFileRepository):
        self.db = db


class MatchCreator(BaseService):
    def __call__(self, data: Match) -> Match:
        return self.db.create(data)


class MatchLister(BaseService):
    def __call__(self, query: str | None = None) -> list[Match]:
        return self.db.list(query)


class MatchRetriever(BaseService):
    def __call__(self, match_id: UUID) -> Match:
        match = self.db.retrieve(match_id)
        if not match:
            raise NotFound
        return match


class MatchUpdater(BaseService):
    def __call__(self, match_id: UUID, data: Match) -> Match:
        return self.db.update(match_id, data)


class MatchDeleter(BaseService):
    def __call__(self, match_id: UUID) -> UUID:
        deleted_id = self.db.delete(match_id)
        if deleted_id is None:
            raise NotFound
        return deleted_id

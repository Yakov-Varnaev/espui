from src.repo import MatchFileRepository


class BaseService:
    def __init__(self, db: MatchFileRepository):
        self.db = db


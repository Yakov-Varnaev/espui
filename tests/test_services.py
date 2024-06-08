from src.models import Match
from src.repo import MatchFileRepository


def test_match_retriever(repository: MatchFileRepository, match_data: dict):
    repository.create(Match(**match_data))
    


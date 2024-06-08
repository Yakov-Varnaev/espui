from pathlib import Path
from uuid import uuid1
import pytest

from src.models import Match
from src.repo import MatchFileRepository


@pytest.fixture
def temp_file() -> Path:
    return Path(__file__).resolve().parent / 'test_data.json'


@pytest.fixture
def repository(temp_file: Path) -> MatchFileRepository:
    return MatchFileRepository(temp_file)


@pytest.fixture
def match(repository: MatchFileRepository) -> Match:
    match = Match(
        trigger='test-trigger',
        replace='test-replace',
    )

    repository.create(match)

    return match


@pytest.fixture
def match_data() -> dict:
    return {
        'trigger': uuid1(),
        'replace': uuid1(),
    }

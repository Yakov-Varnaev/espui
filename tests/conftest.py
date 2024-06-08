import os
from unittest.mock import patch
from pathlib import Path
from typing_extensions import Generator
from uuid import uuid1
import pytest

from src.config import Config
from src.models import Match
from src.repo import MatchFileRepository


pytestmark = [pytest.mark.usefixtures('config')]



@pytest.fixture(scope='function')
def temp_files() -> Generator[tuple[Path, Path], None, None]:
    data_path = Path(__file__).resolve().parent / 'test_data.json'
    yml_path = Path(__file__).resolve().parent / 'test_data.yml'
    yield data_path, yml_path
    os.remove(data_path)
    os.remove(yml_path)


@pytest.fixture
def config(temp_files: tuple[Path, Path]) -> Generator[Config, None, None]:
    file_path, yml_path = temp_files
    config = Config(
        file_path=file_path,
        output_path=yml_path
    )
    with patch('src.dependencies.get_config', return_value=config):
        yield config


@pytest.fixture
def repository(config: Config) -> MatchFileRepository:
    return MatchFileRepository(config.file_path)


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
        'trigger': str(uuid1()),
        'replace': str(uuid1()),
    }

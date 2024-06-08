import yaml
import pytest
from src.config import Config
from src.models import Match
from src.repo import MatchFileRepository
from src.services import MatchCreator
from src.services.espanso import EspansoConfigExporter
from src.services.match import MatchDeleter, MatchLister, MatchRetriever, MatchUpdater


def test_match_creator(repository: MatchFileRepository, match_data: dict):
    service = MatchCreator(repository)
    created_match = service(Match(**match_data))
    match = repository.retrieve(created_match.id)

    assert match is not None
    assert created_match.trigger == match_data['trigger']
    assert created_match.replace == match_data['replace']
    assert created_match.vars is None


def test_match_lister(repository: MatchFileRepository, match: Match):
    service = MatchLister(repository)
    res_matches = service()

    assert res_matches == [match]


def test_match_retriever(repository: MatchFileRepository, match: Match):
    service = MatchRetriever(repository)
    res_match = service(match.id)

    assert res_match == match


def test_match_updater(repository: MatchFileRepository, match: Match):
    service = MatchUpdater(repository)
    res_match = service(match.id, Match(**{**match.model_dump(), 'trigger': 'new-trigger'}))
    cnt = len([*repository.iterator])


    assert cnt == 1
    assert res_match is not None
    assert res_match.id == match.id
    assert res_match.trigger == 'new-trigger'


def test_match_deleter(repository: MatchFileRepository, match: Match):
    service = MatchDeleter(repository)
    res = service(match.id)

    assert res == match.id
    assert repository.retrieve(match.id) is None


def test_espanso_exporter(repository: MatchFileRepository, config: Config, match: Match):
    service = EspansoConfigExporter(repository, config.output_path)
    service()

    assert config.output_path.exists()

    with open(config.output_path, 'r') as f:
        data = yaml.safe_load(f)


    assert data == {'matches': [match.model_dump(exclude_none=True, exclude_unset=True, exclude={'id'})]}


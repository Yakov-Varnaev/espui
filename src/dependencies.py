from fastapi import Depends

from src.config import Config
from src.repo import MatchFileRepository
from src.services.espanso import EspansoConfigExporter
from src.services.match import (
    MatchCreator,
    MatchDeleter,
    MatchLister,
    MatchRetriever,
    MatchUpdater,
)


def get_config() -> Config:
    return Config()


def get_db(cfg: Config = Depends(get_config)) -> MatchFileRepository:
    return MatchFileRepository(cfg.file_path)


def match_creator(db: MatchFileRepository = Depends(get_db)) -> MatchCreator:
    return MatchCreator(db)


def match_lister(db: MatchFileRepository = Depends(get_db)) -> MatchLister:
    return MatchLister(db)


def match_retriver(db: MatchFileRepository = Depends(get_db)) -> MatchRetriever:
    return MatchRetriever(db)


def match_updater(db: MatchFileRepository = Depends(get_db)) -> MatchUpdater:
    return MatchUpdater(db)


def match_deleter(db: MatchFileRepository = Depends(get_db)) -> MatchDeleter:
    return MatchDeleter(db)


def espanso_exporter(
    db: MatchFileRepository = Depends(get_db), config: Config = Depends(get_config)
) -> EspansoConfigExporter:
    return EspansoConfigExporter(db, config.output_path)

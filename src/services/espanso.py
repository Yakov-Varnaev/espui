import logging
from pathlib import Path

from src.models import Match
from src.repo import MatchFileRepository
from src.services.base import BaseService

import yaml


logger = logging.getLogger(__file__)


class EspansoConfigBuilder:
    def __init__(self, output_path: Path | str | None) -> None:
        if output_path is None:
            output_path = Path(__file__).resolve().parent.parent.parent / 'match.yaml'
            logging.info(f'No output path provided defaulting to {output_path}.')
        self.output_path = Path(output_path)

    def export(self, matches: list[Match], force: bool = False) -> None:
        if self.output_path.exists() and not force:
            raise FileExistsError(f'File {self.output_path} already exists.')
        logging.info(f'Exporting espanso config to {self.output_path}.')

        with open(self.output_path, 'w') as f:
            yaml.dump({
                'matches': [
                    m.model_dump(exclude_unset=True, exclude_none=True, exclude={'id'})
                    for m in matches
                ]
            }, f)

        logging.info(f'Espanso config exported succesfully.')


class EspansoConfigExporter(BaseService):
    def __init__(self, repository: MatchFileRepository, output_path: Path | str | None) -> None:
        super().__init__(repository)
        self.builder = EspansoConfigBuilder(output_path)

    def __call__(self, force: bool = False) -> None:
        matches = self.db.list()
        self.builder.export(matches, force)

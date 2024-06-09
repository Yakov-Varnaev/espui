import json
import logging
from pathlib import Path
from uuid import UUID

from typing_extensions import Iterator

from src.encoders import UUIDEncoder
from src.exceptions import JSONFileExpected
from src.models import Match

logger = logging.getLogger(__file__)


class MatchFileRepository:
    """
    Stores data in the specified file.
    """

    def __init__(self, file_path: Path | str | None = None) -> None:
        if file_path is None:
            file_path = Path(__file__).resolve().parent.parent / 'data.json'
        file_path = Path(file_path)
        if file_path.suffix != '.json':
            raise JSONFileExpected()
        self.path = file_path
        self.__create_file()
        self.encoder = UUIDEncoder

    def __create_file(self) -> None:
        logger.info(f'Creating file at: {self.path}.')
        if self.path.exists():
            logger.info('File already exists.')
            return
        with open(self.path, 'w') as f:
            f.write('')
        logger.info(f'File created.')

    def __write_file(self, data: list[Match]) -> None:
        logger.info(f'Writing to file: {self.path}.')
        with open(self.path, 'w') as f:
            json_data = json.dumps(
                [m.model_dump(exclude_none=True) for m in data],
                indent=2,
                cls=UUIDEncoder,
            )
            f.write(json_data)
        logger.info('Wrote to file.')

    def __read_file(self) -> list[Match]:
        with open(self.path, 'r') as f:
            str_data = f.read()
            data = json.loads(str_data) if str_data else []
        assert isinstance(data, list), 'We are fundamentally fucked.'
        return [Match(**m) for m in data]

    @property
    def iterator(self) -> Iterator[Match]:
        for match in self.__read_file():
            yield match

    def create(self, match: Match) -> Match:
        matches = self.__read_file()
        matches.insert(0, match)
        self.__write_file(matches)
        return match

    def list(self, query: str | None = None) -> list[Match]:
        matches = self.__read_file()
        if not query:
            return matches
        return [m for m in matches if query.lower() in m.trigger.lower()]

    def retrieve(self, match_id: UUID) -> Match | None:
        for match in self.iterator:
            if match.id == match_id:
                return match

    def update(self, match_id: UUID, data: Match) -> Match | None:
        res = []
        data.id = match_id
        found = False
        for match in self.iterator:
            if match.id == match_id:
                found = True
                match = data
            res.append(match)
        self.__write_file(res)
        if not found:
            return
        return data

    def delete(self, match_id: UUID) -> UUID | None:
        remaining = []
        deleted = False
        for match in self.iterator:
            if match.id == match_id:
                deleted = True
                continue
            remaining.append(match)
        if deleted:
            self.__write_file(remaining)
            return match_id

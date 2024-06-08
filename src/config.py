from pathlib import Path
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    file_path: Path | str | None = None

    @field_validator('file_path')
    @staticmethod
    def validate_file_path(value: Path | str | None) -> Path | None:
        return Path(value).resolve() if value else None

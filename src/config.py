from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    file_path: Path = Field(
        default=Path(__file__).resolve().parent.parent / 'data.json'
    )
    output_path: Path = Field(
        default=Path(__file__).resolve().parent.parent / 'data.yaml'
    )

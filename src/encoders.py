from json import JSONEncoder
from typing import Any
from uuid import UUID


class UUIDEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, UUID):
            return o.hex
        return super().default(o)


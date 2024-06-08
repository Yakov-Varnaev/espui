from http import HTTPStatus

from fastapi import HTTPException


class JSONFileExpected(Exception):
    message = "Only JSON files are supported."


class NotFound(HTTPException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, status_code=HTTPStatus.NOT_FOUND, **kwargs)


class BadRequest(HTTPException):
    def __init__(self, **kwargs) -> None:
        super().__init__(status_code=HTTPStatus.BAD_REQUEST, **kwargs)

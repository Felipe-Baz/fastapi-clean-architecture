from enum import Enum


class HttpStatus(Enum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER = 500

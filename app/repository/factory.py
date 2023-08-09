from enum import Enum

from app.repository import BaseRepository
from app.repository.memory import MemoryRepository


class Repositories(Enum):
    MEMORY = 1
    FIREBASE = 2


def factory(repo: Repositories) -> BaseRepository:
    match repo:
        case Repositories.MEMORY:
            return MemoryRepository()
        case _:
            raise RuntimeError("Repository not configured")

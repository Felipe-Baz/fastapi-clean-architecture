from typing import Iterable
from pydantic import BaseModel

from app.entity import BaseEntity
from app.entity.user import UserEntity
from app.repository import BaseRepository
from app.use_case import BaseUseCase


def transform(origin: BaseModel) -> BaseEntity:
    return UserEntity.from_dict(origin.model_dump())


class UserListUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self) -> Iterable[BaseEntity]:
        return self.repo.list()


class UserAddUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, other: BaseModel) -> BaseEntity:
        with self.repo as repo:
            return repo.add(transform(other))

from typing import Optional
from typing import TypedDict

from pydantic.dataclasses import dataclass

from app.entity import BaseEntity
from app.repository.memory import MemoryRepository


class Dummy(TypedDict):
    id: Optional[int]


@dataclass
class DummyEntity(BaseEntity):
    @classmethod
    def from_dict(cls, other: dict):
        return cls(id=other["id"])

    def to_dict(self):
        return {"id": self.id}


def test_memory_repository_add_and_list():
    repo = MemoryRepository()
    entity = DummyEntity(id="1")
    other = repo.add(entity)
    entities = repo.list()

    assert other.id == "1"
    assert entities == [entity]


def test_memory_repository_remove():
    repo = MemoryRepository()
    entity = DummyEntity(id="1")
    repo.add(entity)
    result = repo.remove(entity.id)

    assert result


def test_memory_repository_get():
    repo = MemoryRepository()
    entity = DummyEntity(id="1")
    repo.add(entity)
    other = repo.get(entity.id)

    assert other == entity

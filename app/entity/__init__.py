from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[str]

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        pass

    @abstractmethod
    def to_dict(self):
        pass

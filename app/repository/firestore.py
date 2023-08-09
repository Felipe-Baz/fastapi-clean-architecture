from abc import ABC
from typing import Iterable
from typing import Optional
from app.entity import BaseEntity
from app.entity.user import UserEntity
from app.repository import BaseRepository

from google.cloud.firestore import CollectionReference


class FirestoreRepository(BaseRepository, ABC):
    def __init__(self, collection: CollectionReference) -> None:
        self.collection = collection

    def get(self, id: str) -> Optional[BaseEntity]:
        return self.collection.document(id).get()

    def list(self) -> Iterable[BaseEntity]:
        return [
            UserEntity.from_dict(document.to_dict() | {"id": document.id})
            for document in self.collection.get()
        ]

    def add(self, other: BaseEntity) -> BaseEntity:
        _, reference = self.collection.add(other.to_dict())
        other.id = reference.id
        return other

    def remove(self, id: str) -> bool:
        self.collection.document(id).delete()
        return True

    def commit(self) -> None:
        ...

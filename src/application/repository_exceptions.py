from typing import Type, Any
from src.domain.utils import Entity, Id


class EntityNotFound(Exception):
    def __init__(self, entity_type: Type[Entity], message: str):
        self._entity_type = entity_type
        super().__init__(message)

    @property
    def entity_type(self) -> Type[Entity]:
        return self._entity_type


class CannotRetrieveEntity(EntityNotFound):
    def __init__(self, entity_type: Type[Entity], id_: Id) -> None:
        super().__init__(entity_type, f"Cannot retrieve entity of type `{entity_type.__name__}` of id `{id_}`")

from dataclasses import dataclass
from src.domain.utils import Quantity, Id


@dataclass(frozen=True)
class BookCreationRequest:
    id: Id
    title: str
    inventory_quantity: Quantity
    summary: str | None


@dataclass(frozen=True)
class BookUpdateRequest:
    id: Id
    title: str
    inventory_quantity: Quantity
    summary: str | None = None


@dataclass(frozen=True)
class BookDeletionRequest:
    id: Id

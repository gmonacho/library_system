from collections.abc import Collection
from dataclasses import dataclass
from src.domain.utils import Id, Quantity


@dataclass(frozen=True)
class BorrowingResponse:
    customer_id: str


@dataclass(frozen=True)
class BookRetrieveResponse:
    id: Id
    title: str
    inventory_quantity: Quantity
    borrowings: Collection[BorrowingResponse]
    summary: str | None = None

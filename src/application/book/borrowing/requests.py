from dataclasses import dataclass
from src.domain.utils import Id


@dataclass(frozen=True)
class BorrowingCreationRequest:
    book_id: Id
    customer_id: str


@dataclass(frozen=True)
class BorrowingDeletionRequest:
    book_id: Id
    customer_id: str

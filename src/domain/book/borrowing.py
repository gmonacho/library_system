from dataclasses import dataclass


@dataclass(frozen=True)
class Borrowing:
    customer_id: str

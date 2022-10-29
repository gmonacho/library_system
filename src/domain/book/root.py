from src.domain.book.value_objects import Borrowing
from src.domain.utils import Id, Quantity


class Book:
    def __init__(
        self,
        id_: Id,
        title: str,
        inventory_quantity: Quantity,
        summary: str | None,
        borrowings: Borrowing,
    ):
        self._id = id_
        self._title = title
        self._inventory_quantity = inventory_quantity
        self._summary = summary
        self._borrowings = borrowings

    @property
    def id(self) -> Id:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def inventory_quantity(self) -> Quantity:
        return self._inventory_quantity

    @property
    def summary(self) -> str | None:
        return self._summary

    @property
    def borrowings(self) -> Borrowing:
        return self._borrowings

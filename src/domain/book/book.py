from src.domain.book.borrowing import Borrowing
from src.domain.utils import Id, Quantity, Entity


class Book(Entity):
    def __init__(
        self,
        id_: Id,
        title: str,
        inventory_quantity: Quantity,
        summary: str | None,
        borrowings: list[Borrowing],
    ) -> None:
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

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def inventory_quantity(self) -> Quantity:
        return self._inventory_quantity

    @property
    def summary(self) -> str | None:
        return self._summary

    @summary.setter
    def summary(self, value: str | None) -> None:
        self._summary = value

    @property
    def borrowings(self) -> list[Borrowing]:
        return self._borrowings

from src.domain.utils import Id, Quantity, Entity


class Book(Entity):
    def __init__(
        self,
        id_: Id,
        title: str,
        inventory_quantity: Quantity,
        summary: str | None,
        borrowing_ids: list[Id],
    ) -> None:
        self._id = id_
        self._title = title
        self._inventory_quantity = inventory_quantity
        self._summary = summary
        self._borrowing_ids = borrowing_ids

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
    def borrowing_ids(self) -> list[Id]:
        return self._borrowing_ids

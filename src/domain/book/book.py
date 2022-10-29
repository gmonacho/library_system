from src.domain.book.borrowing import Borrowing
from src.domain.book.exceptions import CannotRetrieveBorrowing
from src.domain.utils import Id, Quantity, Entity


class Book(Entity):
    def __init__(
        self,
        id_: Id,
        title: str,
        inventory_quantity: Quantity,
        summary: str | None,
        borrowings: set[Borrowing],
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

    @inventory_quantity.setter
    def inventory_quantity(self, value: Quantity) -> None:
        self._inventory_quantity = value

    @property
    def summary(self) -> str | None:
        return self._summary

    @summary.setter
    def summary(self, value: str | None) -> None:
        self._summary = value

    @property
    def borrowings(self) -> set[Borrowing]:
        return self._borrowings

    # def retrieve_borrowing(self, customer_id: str) -> Borrowing:
    #     """
    #     :param customer_id:
    #     :return: borrowing corresponding to given customer_id
    #     :raises CannotRetrieveBorrowing: if there is no borrowing corresponding to specified customer_id
    #     """

    def add_borrowing(self, borrowing: Borrowing) -> None:
        self._borrowings.add(borrowing)

    def remove_borrowing(self, customer_id: str) -> None:
        """
        :param customer_id:
        :raises CannotRetrieveBorrowing: if there is no borrowing corresponding to specified customer_id
        """
        borrowing_to_remove = Borrowing(customer_id)
        if borrowing_to_remove not in self._borrowings:
            raise CannotRetrieveBorrowing(self._id, customer_id)
        self._borrowings.remove(borrowing_to_remove)

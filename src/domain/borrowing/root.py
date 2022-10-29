import datetime
from src.domain.utils import Id, Entity


class Borrowing(Entity):
    def __init__(
        self,
        id_: Id,
        borrower_first_name: str,
        borrower_last_name: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> None:
        self._id = id_
        self._borrower_first_name = borrower_first_name
        self._borrower_last_name = borrower_last_name
        self._start_date = start_date
        self._end_date = end_date

    @property
    def id(self) -> Id:
        return self._id

    @property
    def borrower_first_name(self) -> str:
        return self._borrower_first_name

    @property
    def borrower_last_name(self) -> str:
        return self._borrower_last_name

    @property
    def start_date(self) -> datetime.datetime:
        return self._start_date

    @property
    def end_date(self) -> datetime.datetime:
        return self._end_date

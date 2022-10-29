import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Borrowing:
    borrower_first_name: str
    borrower_last_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime

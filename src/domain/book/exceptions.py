from src.domain.utils import Id


class CannotRetrieveBorrowing(Exception):
    def __init__(self, book_id: Id, customer_id: str) -> None:
        super().__init__(f"There is no borrowing corresponding to customer_id `{customer_id}` in Book id `{book_id}`")

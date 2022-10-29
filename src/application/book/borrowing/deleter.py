from src.application.book.borrowing.requests import BorrowingDeletionRequest
from src.application.book.ports.repository import BookRepository
from src.application.exceptions import BadRequestException
from src.application.repository_exceptions import CannotRetrieveEntity
from src.domain.book.exceptions import CannotRetrieveBorrowing


class BorrowingDeleter:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def delete(self, borrowing_deletion_request: BorrowingDeletionRequest) -> None:
        try:
            book = self._book_repository.retrieve(borrowing_deletion_request.book_id)
        except CannotRetrieveEntity as err:
            raise BadRequestException("Book id does not belong to an existing entity") from err
        try:
            book.remove_borrowing(borrowing_deletion_request.customer_id)
        except CannotRetrieveBorrowing as err:
            raise BadRequestException(str(err)) from err
        self._book_repository.update(book)

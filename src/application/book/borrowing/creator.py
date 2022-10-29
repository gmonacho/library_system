from src.application.book.borrowing.requests import BorrowingCreationRequest
from src.application.book.ports.repository import BookRepository
from src.application.exceptions import BadRequestException
from src.application.repository_exceptions import CannotRetrieveEntity
from src.domain.book.borrowing import Borrowing


class BorrowingCreator:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def create(self, borrowing_creation_request: BorrowingCreationRequest) -> None:
        try:
            book = self._book_repository.retrieve(borrowing_creation_request.book_id)
        except CannotRetrieveEntity as err:
            raise BadRequestException("Book id does not belong to an existing entity") from err
        book.add_borrowing(Borrowing(borrowing_creation_request.customer_id))
        self._book_repository.update(book)

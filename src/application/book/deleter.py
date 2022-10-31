from src.application.book.ports.repository import BookRepository
from src.application.book.requests import BookDeletionRequest
from src.application.exceptions import BadRequestException
from src.application.repository_exceptions import CannotRetrieveEntity


class BookDeleter:
    def __init__(self, book_repository: BookRepository) -> None:
        self._book_repository = book_repository

    def delete(self, book_deletion_request: BookDeletionRequest) -> None:
        try:
            book = self._book_repository.retrieve(book_deletion_request.id)
        except CannotRetrieveEntity as err:
            raise BadRequestException("Book id does not belong to an existing entity") from err
        if book.borrowings:
            raise BadRequestException("At least one copy of this book is currently in borrowing")
        self._book_repository.delete(book.id)

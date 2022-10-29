from src.application.book.ports.repository import BookRepository
from src.application.book.requests import BookUpdateRequest
from src.application.exceptions import BadRequestException
from src.application.repository_exceptions import CannotRetrieveEntity


class BookUpdater:
    def __init__(self, book_repository: BookRepository) -> None:
        self._book_repository = book_repository

    def update(self, book_update_request: BookUpdateRequest) -> None:
        try:
            book = self._book_repository.retrieve(book_update_request.id)
        except CannotRetrieveEntity as err:
            raise BadRequestException("Book id does not belong to an existing entity") from err
        book.title = book_update_request.title
        book.summary = book_update_request.summary
        self._book_repository.update(book)

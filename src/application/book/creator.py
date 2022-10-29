from src.application.book.ports.repository import BookRepository
from src.application.book.requests import BookCreationRequest
from src.domain.book.root import Book


class BookCreator:
    def __init__(self, book_repository: BookRepository) -> None:
        self._book_repository = book_repository

    def create(self, book_creation_request: BookCreationRequest) -> None:
        book = Book(
            id_=book_creation_request.id,
            title=book_creation_request.title,
            inventory_quantity=book_creation_request.inventory_quantity,
            summary=book_creation_request.summary,
            borrowing_ids=[],
        )
        self._book_repository.create(book)

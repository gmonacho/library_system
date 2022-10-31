from src.application.book.ports.repository import BookRepository
from src.application.book.requests import BookRetrieveRequest
from src.application.book.responses import BookRetrieveResponse, BorrowingResponse
from src.application.exceptions import BadRequestException
from src.application.repository_exceptions import CannotRetrieveEntity


class BookReader:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def retrieve(self, book_retrieve_requests: BookRetrieveRequest) -> BookRetrieveResponse:
        try:
            book = self._book_repository.retrieve(book_id=book_retrieve_requests.id)
        except CannotRetrieveEntity as err:
            raise BadRequestException("Book id does not belong to an existing entity") from err
        return BookRetrieveResponse(
            id=book.id,
            title=book.title,
            inventory_quantity=book.inventory_quantity,
            summary=book.summary,
            borrowings=[BorrowingResponse(br.customer_id) for br in book.borrowings],
        )

    def list_all(self) -> list[BookRetrieveResponse]:
        books = self._book_repository.list_all()
        return [
            BookRetrieveResponse(
                id=book.id,
                title=book.title,
                inventory_quantity=book.inventory_quantity,
                summary=book.summary,
                borrowings=[BorrowingResponse(br.customer_id) for br in book.borrowings],
            )
            for book in books
        ]

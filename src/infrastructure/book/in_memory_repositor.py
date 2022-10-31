import logging
from src.application.book.ports.repository import BookRepository
from src.application.repository_exceptions import CannotRetrieveEntity, EntityAlreadyExists
from src.domain.book.book import Book
from src.domain.utils import Id


class BookInMemoryRepository(BookRepository):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def create(self, book: Book) -> None:
        if book.id in [b.id for b in self._books]:
            raise EntityAlreadyExists(entity_type=Book, id_=book.id)
        self._books.append(book)
        logging.info(self._books)

    def update(self, book: Book) -> None:
        if book.id not in [b.id for b in self._books]:
            raise CannotRetrieveEntity(entity_type=Book, id_=book.id)
        self._books = [b if b.id != book.id else book for b in self._books]

    def delete(self, book_id: Id) -> None:
        if book_id not in [book.id for book in self._books]:
            raise CannotRetrieveEntity(entity_type=Book, id_=book_id)
        self._books = [book for book in self._books if book.id != book_id]

    def retrieve(self, book_id: Id) -> Book:
        try:
            return next(book for book in self._books if book.id == book_id)
        except StopIteration as err:
            raise CannotRetrieveEntity(entity_type=Book, id_=book_id) from err

    def list_all(self) -> list[Book]:
        return self._books

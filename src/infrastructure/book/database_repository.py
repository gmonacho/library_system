import logging
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.application.book.ports.repository import BookRepository
from src.application.repository_exceptions import CannotRetrieveEntity
from src.domain.book.book import Book
from src.domain.book.borrowing import Borrowing
from src.domain.utils import Id, Quantity
from src.infrastructure.book._ean13 import Ean13
from src.infrastructure.book.borrowing.dbo import BorrowingDbo
from src.infrastructure.book.dbo import BookDbo
from src.infrastructure.orm import engine


class BookDatabaseRepository(BookRepository):
    def create(self, book: Book) -> None:
        with Session(engine) as session:
            book_dbo = BookDbo(
                library_id=str(book.id),
                title=book.title,
                inventory_quantity=book.inventory_quantity,
                summary=book.summary,
                borrowings=[BorrowingDbo(customer_id=br.customer_id) for br in book.borrowings],
            )
            session.add(book_dbo)
            session.commit()

    def update(self, book: Book) -> None:
        with Session(engine) as session:
            if not (rows := session.execute(select(BookDbo).where(BookDbo.library_id == str(book.id))).first()):
                raise CannotRetrieveEntity(Book, book.id)
            book_dbo: BookDbo = rows[0]
            book_dbo.library_id = str(book.id)
            book_dbo.title = book.title
            book_dbo.inventory_quantity = book.inventory_quantity
            book_dbo.summary = book.summary
            book_dbo.borrowings = [BorrowingDbo(customer_id=br.customer_id) for br in book.borrowings]
            session.commit()

    def delete(self, book_id: Id) -> None:
        with Session(engine) as session:
            if not (rows := session.execute(select(BookDbo).where(BookDbo.library_id == str(book_id))).first()):
                raise CannotRetrieveEntity(Book, book_id)
            book_dbo: BookDbo = rows[0]
            session.delete(book_dbo)
            session.commit()

    def retrieve(self, book_id: Id) -> Book:
        with Session(engine) as session:
            if not (rows := session.execute(select(BookDbo).where(BookDbo.library_id == str(book_id))).first()):
                raise CannotRetrieveEntity(Book, book_id)
            book_dbo: BookDbo = rows[0]
            return Book(
                id_=Ean13(str(book_dbo.library_id)),
                title=str(book_dbo.title),
                inventory_quantity=Quantity(int(book_dbo.inventory_quantity)),
                summary=str(book_dbo.summary),
                borrowings={Borrowing(str(br_dbo.customer_id)) for br_dbo in book_dbo.borrowings},
            )

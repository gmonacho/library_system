import abc
from src.domain.book.book import Book
from src.domain.utils import Id


class BookRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, book: Book) -> None:
        """
        :param book_id:
        :return:
        :raise EntityAlreadyExists: if entity already exists
        """
        pass

    @abc.abstractmethod
    def update(self, book: Book) -> None:
        """
        :param book_id:
        :return:
        :raise CannotRetrieveEntity: if entity of specified id does not exist
        """
        pass

    @abc.abstractmethod
    def delete(self, book_id: Id) -> None:
        """
        :param book_id:
        :return:
        :raise CannotRetrieveEntity: if entity of specified id does not exist
        """
        pass

    @abc.abstractmethod
    def retrieve(self, book_id: Id) -> Book:
        """
        :param book_id:
        :return:
        :raise CannotRetrieveEntity: if entity of specified id does not exist
        """
        pass

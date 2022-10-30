from flask import Blueprint
import flask_pydantic
import pydantic
from src.application.book.borrowing.creator import BorrowingCreator
from src.application.book.borrowing.deleter import BorrowingDeleter
from src.application.book.borrowing.requests import BorrowingCreationRequest, BorrowingDeletionRequest
from src.infrastructure.book._ean13 import Ean13
from src.infrastructure.book.database_repository import BookDatabaseRepository

borrowing_api = Blueprint("borrowing_api", __name__)


class PostBorrowingBody(pydantic.BaseModel):
    customer_id: str


class PostBorrowingResponse(pydantic.BaseModel):
    pass


@borrowing_api.post("/book/<string:book_id>/borrowing")
@flask_pydantic.validate(body=PostBorrowingBody, on_success_status=201)
def create(book_id: str, body: PostBorrowingBody) -> PostBorrowingResponse:
    try:
        ean = Ean13(book_id)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err
    borrowing_creation_request = BorrowingCreationRequest(book_id=ean, customer_id=body.customer_id)
    BorrowingCreator(BookDatabaseRepository()).create(borrowing_creation_request)
    return PostBorrowingResponse()


class DeleteBorrowingBody(pydantic.BaseModel):
    customer_id: str


class DeleteBorrowingResponse(pydantic.BaseModel):
    pass


@borrowing_api.delete("/book/<string:book_id>/borrowing")
@flask_pydantic.validate(body=DeleteBorrowingBody, on_success_status=200)
def delete(book_id: str, body: DeleteBorrowingBody) -> PostBorrowingResponse:
    try:
        ean = Ean13(book_id)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err
    borrowing_deletion_request = BorrowingDeletionRequest(book_id=ean, customer_id=body.customer_id)
    BorrowingDeleter(BookDatabaseRepository()).delete(borrowing_deletion_request)
    return PostBorrowingResponse()

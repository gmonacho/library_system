import pydantic
import flask_pydantic
from flask import Blueprint
from src.domain.utils import Quantity
from src.application.book.creator import BookCreator
from src.application.book.deleter import BookDeleter
from src.application.book.requests import BookCreationRequest, BookDeletionRequest, BookUpdateRequest
from src.application.book.updater import BookUpdater
from src.infrastructure.book._ean13 import Ean13
from src.infrastructure.book.database_repository import BookDatabaseRepository

book_api = Blueprint("book_api", __name__)


class PostBookBody(pydantic.BaseModel):
    barcode: str
    title: str
    inventory_quantity: pydantic.conint(ge=-1)
    summary: str


class PostBookResponse(pydantic.BaseModel):
    pass


@book_api.post("/book")
@flask_pydantic.validate(on_success_status=201)
def create(body: PostBookBody) -> PostBookResponse:

    try:
        ean = Ean13(body.barcode)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err

    book_creation_request = BookCreationRequest(
        id=ean,
        title=body.title,
        inventory_quantity=Quantity(body.inventory_quantity),
        summary=body.summary,
    )
    BookCreator(BookDatabaseRepository()).create(book_creation_request)
    return PostBookResponse()


class DeleteBookResponse(pydantic.BaseModel):
    pass


@book_api.delete("/book/<string:barcode>")
@flask_pydantic.validate(on_success_status=200)
def delete(barcode: str) -> DeleteBookResponse:

    try:
        ean = Ean13(barcode)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err
    book_deletion_request = BookDeletionRequest(id=ean)
    BookDeleter(BookDatabaseRepository()).delete(book_deletion_request)
    return DeleteBookResponse()


class UpdateBookBody(pydantic.BaseModel):
    title: str
    inventory_quantity: int
    summary: str


class UpdateBookResponse(pydantic.BaseModel):
    pass


@book_api.put("/book/<string:barcode>")
@flask_pydantic.validate(body=UpdateBookBody, on_success_status=200)
def update(barcode: str, body: UpdateBookBody) -> UpdateBookResponse:

    try:
        ean = Ean13(barcode)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err

    book_update_request = BookUpdateRequest(
        id=ean,
        title=body.title,
        inventory_quantity=Quantity(body.inventory_quantity),
        summary=body.summary,
    )
    BookUpdater(BookDatabaseRepository()).update(book_update_request)
    return UpdateBookResponse()

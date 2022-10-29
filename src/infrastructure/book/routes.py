import flask_pydantic
import pydantic
from flask import Blueprint
from pydantic import PositiveInt
from src.application.book.creator import BookCreator
from src.application.book.deleter import BookDeleter
from src.application.book.requests import BookCreationRequest, BookDeletionRequest, BookUpdateRequest
from src.application.book.updater import BookUpdater
from src.domain.utils import Quantity
from src.infrastructure.book._ean13 import Ean13

book_api = Blueprint("book_api", __name__)


class PostBookBody(pydantic.BaseModel):
    barcode: str
    title: str
    inventory_quantity: PositiveInt
    summary: str


@book_api.post("/book")
@flask_pydantic.validate(body=PostBookBody, on_success_status=201)
def create(body: PostBookBody) -> None:
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
    BookCreator().create(book_creation_request)


class DeleteBookBody(pydantic.BaseModel):
    barcode: str


@book_api.delete("/book/<string:barcode>")
@flask_pydantic.validate(body=DeleteBookBody, on_success_status=200)
def delete(body: DeleteBookBody) -> None:
    try:
        ean = Ean13(body.barcode)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err
    book_deletion_request = BookDeletionRequest(id=ean)
    BookDeleter().delete(book_deletion_request)


class UpdateBookBody(pydantic.BaseModel):
    barcode: str
    title: str
    inventory_quantity: int
    summary: str


@book_api.put("/book/<string:barcode>")
@flask_pydantic.validate(body=UpdateBookBody, on_success_status=200)
def update(body: UpdateBookBody) -> None:
    try:
        ean = Ean13(body.barcode)
    except ValueError as err:
        raise ValueError("barcode format is invalid") from err

    book_update_request = BookUpdateRequest(
        id=ean,
        title=body.title,
        inventory_quantity=Quantity(body.inventory_quantity),
        summary=body.summary,
    )
    BookUpdater().update(book_update_request)

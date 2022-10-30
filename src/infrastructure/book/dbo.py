from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import TYPE_CHECKING, List
from src.infrastructure.orm import Base

if TYPE_CHECKING:
    from src.infrastructure.book.borrowing.dbo import BorrowingDbo


class BookDbo(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    library_id = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    inventory_quantity = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    borrowings: Mapped[List["BorrowingDbo"]] = relationship("BorrowingDbo", back_populates="book")

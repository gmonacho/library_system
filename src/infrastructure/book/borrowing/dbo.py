from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from src.infrastructure.book.dbo import BookDbo
from src.infrastructure.orm import Base


class BorrowingDbo(Base):
    __tablename__ = "borrowing"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"), nullable=False)
    customer_id = Column(String, nullable=False)

    book: Mapped[BookDbo] = relationship("BookDbo", back_populates="borrowings")

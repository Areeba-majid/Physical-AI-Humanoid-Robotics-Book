from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database.database import Base


class UserBookAccess(Base):
    __tablename__ = "user_book_access"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    book_id = Column(String, ForeignKey("books.id"), nullable=False)
    access_level = Column(String, default="read")  # read, contribute
    granted_at = Column(DateTime, default=func.now())
    revoked_at = Column(DateTime, nullable=True)
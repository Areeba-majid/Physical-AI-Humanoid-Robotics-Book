from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from src.database.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=True)  # Optional ISBN
    content = Column(Text, nullable=False)  # Full text content
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    metadata = Column(String, nullable=True)  # JSON string for additional metadata
from sqlalchemy import Column, String, Text, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database.database import Base


class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    book_id = Column(String, ForeignKey("books.id"), nullable=False)
    query_text = Column(Text, nullable=False)
    query_mode = Column(String, nullable=False)  # global, section, selection
    section_id = Column(String, ForeignKey("sections.id"), nullable=True)
    selected_text = Column(Text, nullable=True)
    response_text = Column(Text, nullable=False)
    query_timestamp = Column(DateTime, default=func.now())
    response_tokens = Column(Integer, nullable=True)
    processing_time = Column(Float, nullable=True)
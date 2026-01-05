from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.database.database import Base


class Section(Base):
    __tablename__ = "sections"

    id = Column(String, primary_key=True, index=True)
    chapter_id = Column(String, ForeignKey("chapters.id"), nullable=False)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    section_number = Column(Integer, nullable=True)
    start_position = Column(Integer, nullable=False)
    end_position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID


class IngestRequest(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    content: str
    metadata: Optional[Dict[str, Any]] = None


class IngestResponse(BaseModel):
    book_id: str
    title: str
    author: str
    status: str  # processing, completed, failed
    message: str


class BookDetailsResponse(BaseModel):
    id: str
    title: str
    author: str
    isbn: Optional[str] = None
    created_at: str
    chapter_count: int
    word_count: int
    status: str


class ChapterDetails(BaseModel):
    id: str
    title: str
    chapter_number: int
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    section_count: int


class ChaptersResponse(BaseModel):
    book_id: str
    chapters: list[ChapterDetails]
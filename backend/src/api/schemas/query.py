from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class QuerySource(BaseModel):
    chapter_id: str
    chapter_title: str
    section_id: Optional[str] = None
    section_title: Optional[str] = None
    relevance_score: float


class QueryRequest(BaseModel):
    book_id: str
    question: str


class QueryResponse(BaseModel):
    query_id: str
    book_id: str
    question: str
    answer: str
    sources: List[QuerySource]
    processing_time: float


class SectionQueryRequest(BaseModel):
    book_id: str
    section_id: str
    question: str


class SelectionQueryRequest(BaseModel):
    book_id: str
    selected_text: str
    question: str
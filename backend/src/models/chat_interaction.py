"""ChatInteraction model for the AI textbook platform."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class PyObjectId(BaseModel):
    """Custom Pydantic type for MongoDB ObjectId."""
    
    id: str = Field(..., alias="_id")
    
    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class Citation(BaseModel):
    """Model for citations in chat interactions."""
    source: str  # e.g., chapter title, page
    snippet: str
    link: Optional[str] = None


class ChatInteractionBase(BaseModel):
    """Base chat interaction model with common fields."""
    user_id: str
    session_id: str
    user_message: str
    ai_response: str
    citations: List[Citation] = Field(default_factory=list)
    context_used: Optional[str] = None
    feedback_rating: Optional[int] = Field(None, ge=1, le=5)
    feedback_comment: Optional[str] = None


class ChatInteractionCreate(ChatInteractionBase):
    """Model for creating a new chat interaction."""
    pass  # All fields from ChatInteractionBase are required for creation


class ChatInteractionUpdate(BaseModel):
    """Model for updating a chat interaction."""
    feedback_rating: Optional[int] = Field(None, ge=1, le=5)
    feedback_comment: Optional[str] = None


class ChatInteractionInDBBase(ChatInteractionBase):
    """Base chat interaction model with database fields."""
    id: str
    created_at: datetime


class ChatInteraction(ChatInteractionInDBBase):
    """Complete chat interaction model."""
    pass


class ChatInteractionInResponse(BaseModel):
    """ChatInteraction model for API responses."""
    id: str
    user_id: str
    session_id: str
    user_message: str
    ai_response: str
    citations: List[Citation]
    created_at: datetime
    feedback_rating: Optional[int]
    feedback_comment: Optional[str]


class ChatRequest(BaseModel):
    """Model for chat requests."""
    message: str
    session_id: Optional[str] = None
    context: Optional[dict] = None  # Additional context for the query


class ChatResponse(BaseModel):
    """Model for chat responses."""
    id: str
    session_id: str
    user_message: str
    ai_response: str
    citations: List[Citation]
    created_at: datetime
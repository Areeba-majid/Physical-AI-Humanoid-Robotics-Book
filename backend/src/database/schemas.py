"""MongoDB schema definitions for the AI textbook platform.

This module defines the Pydantic models that map to MongoDB collections
following the data model specified in the requirements.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from typing import Literal


class PyObjectId(BaseModel):
    """Custom Pydantic type for MongoDB ObjectId."""
    
    id: str = Field(..., alias="_id")
    
    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class UserBase(BaseModel):
    """Base user model with common fields."""
    email: str
    username: str
    full_name: Optional[str] = None
    preferences: Optional[Dict[str, Any]] = Field(default_factory=dict)
    is_verified: bool = False
    profile_image_url: Optional[str] = None


class UserCreate(UserBase):
    """Model for creating a new user."""
    password: str


class User(UserBase):
    """Complete user model."""
    id: str
    created_at: datetime
    updated_at: datetime
    last_login_at: Optional[datetime] = None


class ChapterBase(BaseModel):
    """Base chapter model with common fields."""
    title: str
    content: str
    content_ur: Optional[str] = None
    sections: List[Dict[str, Any]] = Field(default_factory=list)
    order_index: int
    word_count: Optional[int] = None
    reading_time_estimate: Optional[int] = None  # in minutes
    associated_quiz_id: Optional[str] = None
    status: Literal["published", "draft"] = "draft"
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)


class Chapter(ChapterBase):
    """Complete chapter model."""
    id: str
    created_at: datetime
    updated_at: datetime


class Question(BaseModel):
    """Model for quiz questions."""
    id: str
    question_text: str
    question_type: Literal["mcq", "short_answer"]
    options: List[str] = Field(default_factory=list)  # Only for MCQs
    correct_answer: str
    explanation: Optional[str] = None


class QuizBase(BaseModel):
    """Base quiz model with common fields."""
    title: str
    chapter_id: str
    questions: List[Question] = Field(default_factory=list)
    time_limit: Optional[int] = None  # in seconds
    total_points: int = 0
    difficulty: Literal["beginner", "intermediate", "advanced"] = "beginner"


class Quiz(QuizBase):
    """Complete quiz model."""
    id: str
    created_at: datetime
    updated_at: datetime


class ProgressBase(BaseModel):
    """Base progress model with common fields."""
    user_id: str
    chapter_id: str
    quiz_id: Optional[str] = None
    status: Literal["not_started", "in_progress", "completed"] = "not_started"
    current_position: Optional[int] = 0
    time_spent_seconds: int = 0
    quiz_score: Optional[int] = None
    notes: Optional[str] = None


class Progress(ProgressBase):
    """Complete progress model."""
    id: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    quiz_completed_at: Optional[datetime] = None


class RecommendationBase(BaseModel):
    """Base recommendation model with common fields."""
    user_id: str
    item_id: str
    item_type: Literal["chapter", "quiz", "resource"]
    reason: str
    priority: int = Field(ge=1, le=5)  # 1-5 scale


class Recommendation(RecommendationBase):
    """Complete recommendation model."""
    id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
    clicked_at: Optional[datetime] = None


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


class ChatInteraction(ChatInteractionBase):
    """Complete chat interaction model."""
    id: str
    created_at: datetime


class TranslationBase(BaseModel):
    """Base translation model with common fields."""
    original_content_id: str
    original_language: str
    target_language: str
    translated_content: str
    translator: Optional[str] = None
    status: Literal["pending", "in_review", "approved", "rejected"] = "pending"
    approval_status: Literal["pending", "approved", "rejected"] = "pending"
    approved_by: Optional[str] = None


class Translation(TranslationBase):
    """Complete translation model."""
    id: str
    created_at: datetime
    updated_at: datetime
    approval_date: Optional[datetime] = None
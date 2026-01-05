"""Quiz model for the AI textbook platform."""

from datetime import datetime
from typing import List, Optional
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


class QuizQuestion(BaseModel):
    """Model for a single question within a quiz."""
    id: str
    question_text: str
    question_type: Literal["mcq", "short_answer", "true_false"]
    options: List[str] = Field(default_factory=list)  # Only for MCQ type questions
    correct_answer: str
    explanation: Optional[str] = None
    order_index: int = 0


class QuizBase(BaseModel):
    """Base quiz model with common fields."""
    title: str
    chapter_id: str
    questions: List[QuizQuestion] = Field(default_factory=list)
    time_limit: Optional[int] = None  # in seconds
    total_points: int = 0
    difficulty: Literal["beginner", "intermediate", "advanced"] = "beginner"
    description: Optional[str] = None


class QuizCreate(QuizBase):
    """Model for creating a new quiz."""
    pass  # All fields from QuizBase are required for creation


class QuizUpdate(BaseModel):
    """Model for updating a quiz."""
    title: Optional[str] = None
    chapter_id: Optional[str] = None
    questions: Optional[List[QuizQuestion]] = None
    time_limit: Optional[int] = None
    total_points: Optional[int] = None
    difficulty: Optional[Literal["beginner", "intermediate", "advanced"]] = None
    description: Optional[str] = None


class QuizInDBBase(QuizBase):
    """Base quiz model with database fields."""
    id: str
    created_at: datetime
    updated_at: datetime


class Quiz(QuizInDBBase):
    """Complete quiz model."""
    pass


class QuizInResponse(BaseModel):
    """Quiz model for API responses."""
    id: str
    title: str
    chapter_id: str
    total_points: int
    difficulty: str
    question_count: int
    time_limit: Optional[int]
    created_at: datetime
    updated_at: datetime


class QuizSubmission(BaseModel):
    """Model for submitting quiz answers."""
    answers: List[dict]  # Each dict has question_id and selected_option


class QuizResult(BaseModel):
    """Model for quiz results."""
    quiz_id: str
    user_id: str
    score: int
    max_score: int
    percentage: float
    completed_at: datetime
    time_taken: Optional[int]  # in seconds
    feedback: List[dict] = Field(default_factory=list)  # Detailed feedback for each question
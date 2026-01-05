"""Progress model for the AI textbook platform."""

from datetime import datetime
from typing import Optional
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


class ProgressCreate(ProgressBase):
    """Model for creating a new progress record."""
    pass  # All fields from ProgressBase are required for creation


class ProgressUpdate(BaseModel):
    """Model for updating a progress record."""
    status: Optional[Literal["not_started", "in_progress", "completed"]] = None
    current_position: Optional[int] = None
    time_spent_seconds: Optional[int] = None
    quiz_score: Optional[int] = None
    notes: Optional[str] = None


class ProgressInDBBase(ProgressBase):
    """Base progress model with database fields."""
    id: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    quiz_completed_at: Optional[datetime] = None


class Progress(ProgressInDBBase):
    """Complete progress model."""
    pass


class ProgressInResponse(BaseModel):
    """Progress model for API responses."""
    id: str
    user_id: str
    chapter_id: str
    quiz_id: Optional[str]
    status: str
    current_position: Optional[int]
    time_spent_seconds: int
    quiz_score: Optional[int]
    notes: Optional[str]
    started_at: datetime
    completed_at: Optional[datetime]
    quiz_completed_at: Optional[datetime]
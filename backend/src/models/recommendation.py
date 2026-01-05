"""Recommendation model for the AI textbook platform."""

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


class RecommendationBase(BaseModel):
    """Base recommendation model with common fields."""
    user_id: str
    item_id: str
    item_type: Literal["chapter", "quiz", "resource", "topic"]
    reason: str
    priority: int = Field(ge=1, le=5)  # 1-5 scale


class RecommendationCreate(RecommendationBase):
    """Model for creating a new recommendation."""
    pass  # All fields from RecommendationBase are required for creation


class RecommendationUpdate(BaseModel):
    """Model for updating a recommendation."""
    reason: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=5)  # 1-5 scale


class RecommendationInDBBase(RecommendationBase):
    """Base recommendation model with database fields."""
    id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
    clicked_at: Optional[datetime] = None


class Recommendation(RecommendationInDBBase):
    """Complete recommendation model."""
    pass


class RecommendationInResponse(BaseModel):
    """Recommendation model for API responses."""
    id: str
    user_id: str
    item_id: str
    item_type: str
    reason: str
    priority: int
    created_at: datetime
    viewed_at: Optional[datetime]
    clicked_at: Optional[datetime]
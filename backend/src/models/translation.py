"""Translation model for the AI textbook platform."""

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


class TranslationCreate(TranslationBase):
    """Model for creating a new translation."""
    pass  # All fields from TranslationBase are required for creation


class TranslationUpdate(BaseModel):
    """Model for updating a translation."""
    translated_content: Optional[str] = None
    translator: Optional[str] = None
    status: Optional[Literal["pending", "in_review", "approved", "rejected"]] = None
    approval_status: Optional[Literal["pending", "approved", "rejected"]] = None
    approved_by: Optional[str] = None


class TranslationInDBBase(TranslationBase):
    """Base translation model with database fields."""
    id: str
    created_at: datetime
    updated_at: datetime
    approval_date: Optional[datetime] = None


class Translation(TranslationInDBBase):
    """Complete translation model."""
    pass


class TranslationInResponse(BaseModel):
    """Translation model for API responses."""
    id: str
    original_content_id: str
    original_language: str
    target_language: str
    translated_content: str
    translator: Optional[str]
    status: str
    approval_status: str
    approved_by: Optional[str]
    created_at: datetime
    updated_at: datetime
    approval_date: Optional[datetime]
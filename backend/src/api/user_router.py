"""User management API router for the AI textbook platform."""

from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
import secrets
from datetime import datetime

from src.database.schemas import User, Progress, Recommendation
from src.database.repository import BaseRepository
from fastapi.security import HTTPBearer

# Security scheme for authentication
security_scheme = HTTPBearer()

router = APIRouter()

# Mock repositories for demonstration
class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, "users")

class ProgressRepository(BaseRepository[Progress]):
    def __init__(self):
        super().__init__(Progress, "progress")

class RecommendationRepository(BaseRepository[Recommendation]):
    def __init__(self):
        super().__init__(Recommendation, "recommendations")

@router.get("/{user_id}/progress", response_model=List[Progress])
async def get_user_progress(
    user_id: str,
    chapter_id: Optional[str] = None,
    token: str = Depends(security_scheme)
):
    """Retrieve the learning progress for a user."""
    progress_repo = ProgressRepository()
    
    # Create filter for user's progress
    filter_dict = {"user_id": user_id}
    
    # If chapter_id is specified, filter by that chapter
    if chapter_id:
        filter_dict["chapter_id"] = chapter_id
    
    progress_list = await progress_repo.find_many(filter_dict)
    
    return progress_list

@router.post("/{user_id}/progress")
async def update_user_progress(
    user_id: str,
    chapter_id: str,
    status: str,
    current_position: Optional[int] = 0,
    time_spent_seconds: int = 0,
    notes: Optional[str] = None,
    token: str = Depends(security_scheme)
):
    """Update the learning progress for a user."""
    # Validate status
    valid_statuses = ["not_started", "in_progress", "completed"]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Status must be one of: {valid_statuses}"
        )
    
    progress_repo = ProgressRepository()
    
    # Check if a progress record already exists for this user and chapter
    existing_progress = await progress_repo.find_one({
        "user_id": user_id,
        "chapter_id": chapter_id
    })
    
    if existing_progress:
        # Update existing progress
        update_data = {
            "status": status,
            "current_position": current_position,
            "time_spent_seconds": time_spent_seconds
        }
        if notes:
            update_data["notes"] = notes
            
        updated_progress = await progress_repo.update(existing_progress.id, update_data)
        return updated_progress
    else:
        # Create new progress record
        progress = Progress(
            id=secrets.token_hex(8),
            user_id=user_id,
            chapter_id=chapter_id,
            status=status,
            current_position=current_position,
            time_spent_seconds=time_spent_seconds,
            notes=notes or "",
            started_at=datetime.utcnow()
        )
        
        if status == "completed":
            progress.completed_at = datetime.utcnow()
        
        created_progress = await progress_repo.create(progress)
        return created_progress

@router.get("/{user_id}/recommendations", response_model=List[Recommendation])
async def get_user_recommendations(
    user_id: str,
    token: str = Depends(security_scheme)
):
    """Retrieve personalized content recommendations for a user."""
    recommendation_repo = RecommendationRepository()
    
    # Get recommendations for this user
    recommendations = await recommendation_repo.find_many({"user_id": user_id})
    
    # Sort by priority (highest first)
    recommendations.sort(key=lambda x: x.priority, reverse=True)
    
    return recommendations

@router.put("/{user_id}/preferences")
async def update_user_preferences(
    user_id: str,
    preferences: dict,
    token: str = Depends(security_scheme)
):
    """Update user preferences."""
    user_repo = UserRepository()
    
    user = await user_repo.find_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    # Update user preferences
    updated_user = await user_repo.update(user_id, {"preferences": preferences})
    
    return {"message": "Preferences updated successfully", "user": updated_user}
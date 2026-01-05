"""Textbook content router for the AI textbook platform."""

from fastapi import APIRouter, Query, HTTPException, status, Depends
from typing import List, Optional
from datetime import datetime

from src.models.chapter import Chapter
from src.services.chapter_service import ChapterService
from src.utils.exceptions import ChapterNotFoundException
from fastapi.security import HTTPBearer

# Security scheme for authentication (for protected endpoints)
security_scheme = HTTPBearer()

router = APIRouter()

@router.get("/", response_model=List[Chapter])
async def get_chapters(
    language: str = Query("en", description="Language code (e.g., en, ur)"),
    limit: int = Query(10, ge=1, le=50, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """Retrieve a list of all available textbook chapters."""
    chapter_service = ChapterService()

    # Get all published chapters with pagination
    chapters = await chapter_service.get_published_chapters(skip=offset, limit=limit)

    return chapters

@router.get("/{id}", response_model=Chapter)
async def get_chapter(
    id: str,
    language: str = Query("en", description="Language code (e.g., en, ur)")
):
    """Retrieve a specific chapter by ID."""
    chapter_service = ChapterService()

    try:
        chapter = await chapter_service.get_chapter_by_id(id)
        return chapter
    except ChapterNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID {id} not found"
        )

@router.get("/{id}/urdu", response_model=Chapter)
async def get_chapter_urdu(id: str):
    """Retrieve the Urdu translation of a chapter."""
    chapter_service = ChapterService()

    try:
        chapter = await chapter_service.get_chapter_by_id(id)

        # Check if Urdu content exists
        if not chapter.content_ur:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Urdu translation not available for chapter {id}"
            )

        # Return the chapter with Urdu content (in a real implementation, you might want to return a different model)
        return chapter

    except ChapterNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID {id} not found"
        )

@router.get("/order/{order_index}", response_model=Chapter)
async def get_chapter_by_order_index(order_index: int):
    """Retrieve a chapter by its order index."""
    chapter_service = ChapterService()

    try:
        chapter = await chapter_service.get_chapter_by_order_index(order_index)
        return chapter
    except ChapterNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with order index {order_index} not found"
        )

@router.get("/{id}/next", response_model=Optional[Chapter])
async def get_next_chapter(id: str):
    """Retrieve the next chapter after the specified one."""
    chapter_service = ChapterService()

    try:
        current_chapter = await chapter_service.get_chapter_by_id(id)
        next_chapter = await chapter_service.get_next_chapter(current_chapter.order_index)
        return next_chapter
    except ChapterNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID {id} not found"
        )

@router.get("/{id}/previous", response_model=Optional[Chapter])
async def get_previous_chapter(id: str):
    """Retrieve the previous chapter before the specified one."""
    chapter_service = ChapterService()

    try:
        current_chapter = await chapter_service.get_chapter_by_id(id)
        prev_chapter = await chapter_service.get_previous_chapter(current_chapter.order_index)
        return prev_chapter
    except ChapterNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter with ID {id} not found"
        )

# Additional endpoints for textbook management can be added here as needed
# For example: creating, updating, or deleting chapters by authorized users
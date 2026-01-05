"""Chatbot API router for the AI textbook platform."""

from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
from datetime import datetime

from src.models.chat_interaction import ChatInteraction
from src.services.rag_service import RAGService
from src.utils.exceptions import AIServiceException
from fastapi.security import HTTPBearer

# Security scheme for authentication
security_scheme = HTTPBearer()

router = APIRouter()


@router.post("/", response_model=ChatInteraction)
async def send_message_to_chatbot(
    message: str,
    session_id: Optional[str] = None,
    context: Optional[dict] = None,
    token: str = Depends(security_scheme)
):
    """Send a message to the RAG chatbot and receive a response."""

    # For this example, we'll use a mock user_id
    # In a real implementation, get from token
    user_id = "mock_user_id"

    try:
        rag_service = RAGService()
        chat_interaction = await rag_service.generate_response(
            user_message=message,
            user_id=user_id,
            session_id=session_id or "",
            context=context
        )

        return chat_interaction
    except AIServiceException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI service error: {e.message}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )


@router.get("/{session_id}", response_model=List[ChatInteraction])
async def get_chat_history(
    session_id: str,
    token: str = Depends(security_scheme)
):
    """Retrieve chat history for a session."""

    try:
        rag_service = RAGService()
        interactions = await rag_service.get_chat_history(session_id)

        return interactions
    except AIServiceException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI service error: {e.message}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving chat history"
        )


@router.post("/feedback")
async def submit_chat_feedback(
    interaction_id: str,
    rating: int,
    comment: Optional[str] = None,
    token: str = Depends(security_scheme)
):
    """Submit feedback for a specific chat interaction."""
    if rating < 1 or rating > 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Rating must be between 1 and 5"
        )

    try:
        rag_service = RAGService()
        success = await rag_service.save_feedback(interaction_id, rating, comment)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Interaction with ID {interaction_id} not found"
            )

        return {"message": "Feedback submitted successfully"}
    except AIServiceException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI service error: {e.message}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while submitting feedback"
        )
"""Quiz API router for the AI textbook platform."""

from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
import secrets
from datetime import datetime

from src.database.schemas import Quiz, Question
from src.database.repository import BaseRepository
from fastapi.security import HTTPBearer

# Security scheme for authentication
security_scheme = HTTPBearer()

router = APIRouter()

# Mock quiz repository for demonstration
class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        super().__init__(Quiz, "quizzes")

    async def get_by_chapter_id(self, chapter_id: str) -> Optional[Quiz]:
        """Get quiz associated with a specific chapter."""
        return await self.find_one({"chapter_id": chapter_id})

@router.get("/{chapter_id}", response_model=Quiz)
async def get_quiz_for_chapter(
    chapter_id: str,
    token: str = Depends(security_scheme)
):
    """Retrieve the quiz associated with a chapter."""
    quiz_repo = QuizRepository()
    
    quiz = await quiz_repo.get_by_chapter_id(chapter_id)
    
    if not quiz:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No quiz found for chapter {chapter_id}"
        )
    
    return quiz

@router.post("/{quiz_id}/submit")
async def submit_quiz_answers(
    quiz_id: str,
    answers: List[dict],  # Each dict has question_id and selected_option
    token: str = Depends(security_scheme)
):
    """Submit answers for a quiz."""
    quiz_repo = QuizRepository()
    
    quiz = await quiz_repo.find_by_id(quiz_id)
    if not quiz:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Quiz with ID {quiz_id} not found"
        )
    
    # Calculate score - this is a simplified implementation
    correct_answers = 0
    total_questions = len(quiz.questions)
    
    # In a real implementation, we would match the submitted answers with the quiz questions
    # For this example, I'll calculate a mock score
    for answer in answers:
        question_id = answer.get("question_id")
        selected_option = answer.get("selected_option")
        
        # Find the corresponding question in the quiz
        question = next((q for q in quiz.questions if q.id == question_id), None)
        if question and question.correct_answer == selected_option:
            correct_answers += 1
    
    score = correct_answers
    percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    # In a real implementation, we would save the results to the progress collection
    # For this example, we'll just return the mock results
    results = {
        "quiz_id": quiz_id,
        "user_id": "mock_user_id",  # In a real implementation, get from token
        "score": score,
        "max_score": total_questions,
        "percentage": round(percentage, 2),
        "feedback": []  # Detailed feedback for each question
    }
    
    return results

@router.get("/{quiz_id}/results")
async def get_quiz_results(
    quiz_id: str,
    token: str = Depends(security_scheme)
):
    """Retrieve quiz results for a user."""
    # In a real implementation, this would fetch the user's quiz results from the progress collection
    # For this example, we'll return a mock response
    return {
        "quiz_id": quiz_id,
        "user_id": "mock_user_id",  # In a real implementation, get from token
        "attempts": 1,
        "best_score": 8,
        "average_score": 8,
        "completed_at": datetime.utcnow()
    }
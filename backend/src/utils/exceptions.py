"""Custom exception classes for the AI textbook platform."""

from typing import Optional
from fastapi import HTTPException, status


class BaseAppException(Exception):
    """Base exception class for the application."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class UserNotFoundException(BaseAppException):
    """Exception raised when a user is not found."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found", "USER_NOT_FOUND")


class ChapterNotFoundException(BaseAppException):
    """Exception raised when a chapter is not found."""
    
    def __init__(self, chapter_id: str):
        self.chapter_id = chapter_id
        super().__init__(f"Chapter with ID {chapter_id} not found", "CHAPTER_NOT_FOUND")


class QuizNotFoundException(BaseAppException):
    """Exception raised when a quiz is not found."""
    
    def __init__(self, quiz_id: str):
        self.quiz_id = quiz_id
        super().__init__(f"Quiz with ID {quiz_id} not found", "QUIZ_NOT_FOUND")


class AuthenticationException(BaseAppException):
    """Exception raised for authentication-related errors."""
    
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, "AUTH_ERROR")


class AuthorizationException(BaseAppException):
    """Exception raised for authorization-related errors."""
    
    def __init__(self, message: str = "Authorization failed"):
        super().__init__(message, "AUTHZ_ERROR")


class InvalidCredentialsException(BaseAppException):
    """Exception raised when invalid credentials are provided."""
    
    def __init__(self):
        super().__init__("Invalid email or password", "INVALID_CREDENTIALS")


class DuplicateUserException(BaseAppException):
    """Exception raised when trying to create a duplicate user."""
    
    def __init__(self, email: str):
        super().__init__(f"User with email {email} already exists", "DUPLICATE_USER")


class ValidationError(BaseAppException):
    """Exception raised for validation errors."""
    
    def __init__(self, message: str):
        super().__init__(message, "VALIDATION_ERROR")


class DatabaseException(BaseAppException):
    """Exception raised for database-related errors."""
    
    def __init__(self, message: str):
        super().__init__(f"Database error: {message}", "DB_ERROR")


class AIServiceException(BaseAppException):
    """Exception raised for AI service-related errors."""
    
    def __init__(self, message: str):
        super().__init__(f"AI service error: {message}", "AI_SERVICE_ERROR")


class EmbeddingException(BaseAppException):
    """Exception raised for embedding-related errors."""
    
    def __init__(self, message: str):
        super().__init__(f"Embedding error: {message}", "EMBEDDING_ERROR")


class FileUploadException(BaseAppException):
    """Exception raised for file upload errors."""
    
    def __init__(self, message: str):
        super().__init__(f"File upload error: {message}", "FILE_UPLOAD_ERROR")


def create_http_exception(
    status_code: int,
    detail: str,
    headers: Optional[dict] = None
) -> HTTPException:
    """Helper function to create HTTP exceptions."""
    return HTTPException(
        status_code=status_code,
        detail=detail,
        headers=headers
    )


def create_bad_request_exception(detail: str) -> HTTPException:
    """Helper function to create a 400 Bad Request exception."""
    return create_http_exception(status.HTTP_400_BAD_REQUEST, detail)


def create_unauthorized_exception(detail: str = "Not authenticated") -> HTTPException:
    """Helper function to create a 401 Unauthorized exception."""
    return create_http_exception(status.HTTP_401_UNAUTHORIZED, detail)


def create_forbidden_exception(detail: str = "Access forbidden") -> HTTPException:
    """Helper function to create a 403 Forbidden exception."""
    return create_http_exception(status.HTTP_403_FORBIDDEN, detail)


def create_not_found_exception(detail: str) -> HTTPException:
    """Helper function to create a 404 Not Found exception."""
    return create_http_exception(status.HTTP_404_NOT_FOUND, detail)


def create_conflict_exception(detail: str) -> HTTPException:
    """Helper function to create a 409 Conflict exception."""
    return create_http_exception(status.HTTP_409_CONFLICT, detail)


def create_internal_error_exception(detail: str = "Internal server error") -> HTTPException:
    """Helper function to create a 500 Internal Server Error exception."""
    return create_http_exception(status.HTTP_500_INTERNAL_SERVER_ERROR, detail)
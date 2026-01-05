"""Error handling middleware for the AI textbook platform."""

import traceback
import logging
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Callable, Any

from .exceptions import (
    BaseAppException,
    UserNotFoundException,
    ChapterNotFoundException,
    QuizNotFoundException,
    AuthenticationException,
    AuthorizationException,
    InvalidCredentialsException,
    DuplicateUserException,
    ValidationError,
    DatabaseException,
    AIServiceException,
    EmbeddingException,
    FileUploadException
)
from .logging import log_exception, app_logger


def exception_handler_middleware():
    """Middleware to handle exceptions globally in the application."""
    
    async def dispatch(request: Request, call_next: Callable) -> Any:
        try:
            response = await call_next(request)
            return response
        except HTTPException as e:
            # Log the HTTP exception
            app_logger.warning(
                f"HTTP Exception: {e.status_code} - {e.detail}",
                request_id=request.headers.get("X-Request-ID"),
                context={
                    "path": request.url.path,
                    "method": request.method,
                    "status_code": e.status_code
                }
            )
            return JSONResponse(
                status_code=e.status_code,
                content={"detail": e.detail}
            )
        except BaseAppException as e:
            # Log application-specific exceptions
            log_exception(
                e,
                request.headers.get("X-User-ID"),
                request.headers.get("X-Request-ID"),
                {
                    "path": request.url.path,
                    "method": request.method
                }
            )
            
            # Map application exceptions to HTTP status codes
            status_code = 500  # Default to internal server error
            if isinstance(e, (UserNotFoundException, ChapterNotFoundException, QuizNotFoundException)):
                status_code = 404
            elif isinstance(e, (AuthenticationException, InvalidCredentialsException)):
                status_code = 401
            elif isinstance(e, (AuthorizationException,)):
                status_code = 403
            elif isinstance(e, (DuplicateUserException,)):
                status_code = 409
            elif isinstance(e, (ValidationError,)):
                status_code = 400
            
            return JSONResponse(
                status_code=status_code,
                content={
                    "error_code": e.error_code,
                    "message": e.message
                }
            )
        except Exception as e:
            # Log unhandled exceptions
            request_id = request.headers.get("X-Request-ID")
            user_id = request.headers.get("X-User-ID")
            
            app_logger.exception(
                f"Unhandled Exception: {str(e)}",
                request_id=request_id,
                user_id=user_id,
                context={
                    "path": request.url.path,
                    "method": request.method,
                    "exception_type": type(e).__name__,
                    "traceback": traceback.format_exc()
                }
            )
            
            # Return a generic error response to avoid exposing internal details
            return JSONResponse(
                status_code=500,
                content={
                    "error_code": "INTERNAL_ERROR",
                    "message": "An internal error occurred"
                }
            )

    return dispatch


# Custom exception handlers for specific exception types
async def handle_user_not_found_exception(request: Request, exc: UserNotFoundException):
    """Handle UserNotFoundException."""
    app_logger.warning(
        f"User not found: {exc.user_id}",
        user_id=exc.user_id,
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=404,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


async def handle_chapter_not_found_exception(request: Request, exc: ChapterNotFoundException):
    """Handle ChapterNotFoundException."""
    app_logger.warning(
        f"Chapter not found: {exc.chapter_id}",
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=404,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


async def handle_quiz_not_found_exception(request: Request, exc: QuizNotFoundException):
    """Handle QuizNotFoundException."""
    app_logger.warning(
        f"Quiz not found: {exc.quiz_id}",
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=404,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


async def handle_authentication_exception(request: Request, exc: AuthenticationException):
    """Handle AuthenticationException."""
    app_logger.warning(
        "Authentication failed",
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=401,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


async def handle_authorization_exception(request: Request, exc: AuthorizationException):
    """Handle AuthorizationException."""
    app_logger.warning(
        "Authorization failed",
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=403,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


async def handle_validation_exception(request: Request, exc: ValidationError):
    """Handle ValidationError."""
    app_logger.warning(
        f"Validation error: {exc.message}",
        request_id=request.headers.get("X-Request-ID")
    )
    
    return JSONResponse(
        status_code=400,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


# Mapping of exception types to their handlers
EXCEPTION_HANDLERS = {
    UserNotFoundException: handle_user_not_found_exception,
    ChapterNotFoundException: handle_chapter_not_found_exception,
    QuizNotFoundException: handle_quiz_not_found_exception,
    AuthenticationException: handle_authentication_exception,
    AuthorizationException: handle_authorization_exception,
    ValidationError: handle_validation_exception,
}
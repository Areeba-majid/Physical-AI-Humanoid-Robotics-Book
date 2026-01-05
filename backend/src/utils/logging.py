"""Logging infrastructure for the AI textbook platform."""

import logging
import sys
from enum import Enum
from typing import Optional
from datetime import datetime
import json
from logging.handlers import RotatingFileHandler

from .exceptions import BaseAppException


class LogLevel(Enum):
    """Log level enum."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LogFormatter(logging.Formatter):
    """Custom log formatter for the application."""
    
    def format(self, record):
        # Create a custom log format
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        # Add extra fields if present
        if hasattr(record, "user_id"):
            log_entry["user_id"] = record.user_id
        if hasattr(record, "request_id"):
            log_entry["request_id"] = record.request_id
        if hasattr(record, "context"):
            log_entry["context"] = record.context
        
        return json.dumps(log_entry)


class AppLogger:
    """Application logger with structured logging."""
    
    def __init__(self, name: str, log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Prevent adding multiple handlers if logger already has handlers
        if self.logger.handlers:
            return
            
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_formatter = LogFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # Create file handler if log_file is specified
        if log_file:
            file_handler = RotatingFileHandler(
                log_file, maxBytes=10*1024*1024, backupCount=5  # 10MB max, 5 backups
            )
            file_handler.setLevel(logging.DEBUG)
            file_formatter = LogFormatter()
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
    
    def debug(self, message: str, user_id: Optional[str] = None, 
              request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log a debug message."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.debug(message, extra=extra)
    
    def info(self, message: str, user_id: Optional[str] = None, 
             request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log an info message."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.info(message, extra=extra)
    
    def warning(self, message: str, user_id: Optional[str] = None, 
                request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log a warning message."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.warning(message, extra=extra)
    
    def error(self, message: str, user_id: Optional[str] = None, 
              request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log an error message."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.error(message, extra=extra)
    
    def critical(self, message: str, user_id: Optional[str] = None, 
                 request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log a critical message."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.critical(message, extra=extra)
    
    def exception(self, message: str, user_id: Optional[str] = None, 
                  request_id: Optional[str] = None, context: Optional[dict] = None, **kwargs):
        """Log an exception with traceback."""
        extra = self._build_extra(user_id, request_id, context)
        extra.update(kwargs)
        self.logger.exception(message, extra=extra)
    
    def _build_extra(self, user_id: Optional[str], request_id: Optional[str], context: Optional[dict]):
        """Build the extra fields for logging."""
        extra = {}
        if user_id:
            extra["user_id"] = user_id
        if request_id:
            extra["request_id"] = request_id
        if context:
            extra["context"] = context
        return extra


# Create a global logger instance for the application
app_logger = AppLogger("ai_textbook_platform", "logs/app.log")


def log_exception(exception: BaseAppException, user_id: Optional[str] = None, 
                  request_id: Optional[str] = None, context: Optional[dict] = None):
    """Log an application exception with structured details."""
    app_logger.error(
        f"Application Exception: {exception.error_code} - {exception.message}",
        user_id=user_id,
        request_id=request_id,
        context=context,
        exception_type=type(exception).__name__,
        error_code=exception.error_code
    )


def log_api_call(endpoint: str, method: str, user_id: Optional[str] = None, 
                 request_id: Optional[str] = None, response_time: Optional[float] = None):
    """Log an API call with relevant details."""
    app_logger.info(
        f"API Call: {method} {endpoint}",
        user_id=user_id,
        request_id=request_id,
        response_time_ms=response_time,
        endpoint=endpoint,
        method=method
    )


def log_user_action(action: str, user_id: str, request_id: Optional[str] = None, 
                    context: Optional[dict] = None):
    """Log a user action for audit trail."""
    app_logger.info(
        f"User Action: {action}",
        user_id=user_id,
        request_id=request_id,
        context=context,
        action=action
    )


def log_ai_interaction(user_query: str, ai_response: str, user_id: Optional[str] = None, 
                       session_id: Optional[str] = None, context: Optional[dict] = None):
    """Log an AI interaction for analytics and debugging."""
    app_logger.info(
        f"AI Interaction",
        user_id=user_id,
        session_id=session_id,
        context=context,
        query=user_query,
        response=ai_response[:100] + "..." if len(ai_response) > 100 else ai_response  # Truncate long responses
    )


def log_db_operation(operation: str, collection: str, user_id: Optional[str] = None,
                     request_id: Optional[str] = None, context: Optional[dict] = None):
    """Log a database operation."""
    app_logger.info(
        f"DB Operation: {operation} on {collection}",
        user_id=user_id,
        request_id=request_id,
        context=context,
        operation=operation,
        collection=collection
    )


def setup_logging():
    """Setup logging configuration for the application."""
    # Ensure log directory exists
    import os
    os.makedirs("logs", exist_ok=True)
    
    # Basic configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Return the configured logger
    return app_logger
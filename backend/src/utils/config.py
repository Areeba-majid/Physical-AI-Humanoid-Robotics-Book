"""Configuration management for the AI textbook platform."""

import os
from typing import Optional
from pydantic import BaseModel, BaseSettings, validator
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


class Settings(BaseModel):
    """Application settings loaded from environment variables."""
    
    # Database Configuration
    mongodb_uri: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    database_name: str = os.getenv("DATABASE_NAME", "textbook_platform")
    
    # Qdrant Configuration
    qdrant_url: str = os.getenv("QDRANT_URL", "")
    qdrant_api_key: Optional[str] = os.getenv("QDRANT_API_KEY")
    
    # AI/ML Configuration
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    
    # Application Configuration
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    port: int = int(os.getenv("PORT", "8000"))
    
    # Redis Configuration (for caching)
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Security Configuration
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your-super-secret-jwt-key")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Rate Limiting
    rate_limit_requests: int = int(os.getenv("RATE_LIMIT_REQUESTS", "100"))
    rate_limit_window: int = int(os.getenv("RATE_LIMIT_WINDOW", "3600"))
    
    # File Upload Configuration
    max_file_size: int = int(os.getenv("MAX_FILE_SIZE", "10485760"))  # 10MB
    allowed_file_extensions: str = os.getenv("ALLOWED_FILE_EXTENSIONS", "pdf,doc,docx")
    upload_path: str = os.getenv("UPLOAD_PATH", "./uploads")
    
    # Email Configuration (for notifications)
    email_host: str = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    email_port: int = int(os.getenv("EMAIL_PORT", "587"))
    email_username: Optional[str] = os.getenv("EMAIL_USERNAME")
    email_password: Optional[str] = os.getenv("EMAIL_PASSWORD")
    
    # External API Keys
    news_api_key: Optional[str] = os.getenv("NEWS_API_KEY")
    
    # Validators
    @validator('mongodb_uri')
    def mongodb_uri_must_be_set(cls, v):
        if not v:
            raise ValueError('MONGODB_URI must be set')
        return v
    
    @validator('database_name')
    def database_name_must_be_set(cls, v):
        if not v:
            raise ValueError('DATABASE_NAME must be set')
        return v

    @validator('gemini_api_key')
    def gemini_api_key_must_be_set(cls, v):
        if not v:
            raise ValueError('GEMINI_API_KEY must be set')
        return v
    
    @validator('jwt_secret_key')
    def jwt_secret_key_must_not_be_default(cls, v):
        if v == "your-super-secret-jwt-key":
            raise ValueError('JWT_SECRET_KEY must be set to a secure value')
        return v

    class Config:
        case_sensitive = True


# Create a singleton instance of settings
def get_settings():
    """Get the application settings."""
    return Settings()


# Export the settings instance
settings = get_settings()
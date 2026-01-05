from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    # Application settings
    PROJECT_NAME: str = "RAG Chatbot API"
    API_V1_STR: str = "/v1"
    DEBUG: bool = False
    
    # Security settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database settings
    NEON_DATABASE_URL: str
    
    # Qdrant settings
    QDRANT_CLUSTER_URL: str
    QDRANT_API_KEY: str
    
    # API Keys
    OPENAI_API_KEY: str
    COHERE_API_KEY: str
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["*"]  # Should be restricted in production
    
    # Application settings
    MAX_CONTENT_LENGTH: int = 5000  # Maximum length of user-selected text
    CHUNK_SIZE: int = 1000  # Size of text chunks for embedding
    SIMILARITY_THRESHOLD: float = 0.7  # Minimum similarity score for retrieval
    
    class Config:
        env_file = ".env"


settings = Settings()
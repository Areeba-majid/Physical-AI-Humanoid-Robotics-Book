from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from typing import AsyncGenerator
from src.api.dependencies import get_current_user
from src.models.user import User
from src.config import settings
from src.api.routes import ingest, query, selection_query
from src.api.chat_router import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup logic here
    print("Starting up RAG Chatbot API...")
    
    # Initialize services if needed
    # Example: await initialize_database()
    
    yield
    
    # Shutdown logic here
    print("Shutting down RAG Chatbot API...")


app = FastAPI(
    title="RAG Chatbot API",
    description="API for Retrieval-Augmented Generation chatbot embedded in books",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(ingest.router, prefix="/v1", tags=["ingestion"])
app.include_router(query.router, prefix="/v1", tags=["query"])
app.include_router(selection_query.router, prefix="/v1", tags=["selection_query"])
app.include_router(chat_router, prefix="/v1/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "RAG Chatbot API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Protected endpoint example
@app.get("/user/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
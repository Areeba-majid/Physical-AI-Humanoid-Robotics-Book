# Quickstart Guide: Integrated RAG Chatbot Development

**Feature**: 001-rag-chatbot-spec
**Date**: 2025-12-17

## Overview
This guide provides a quick overview of how to set up and start using the RAG chatbot system for book interaction.

## Prerequisites
- Python 3.11 installed
- Access to OpenAI API (with appropriate subscription)
- Access to Cohere API
- Access to Qdrant Cloud (Free Tier)
- Neon Serverless Postgres database

## Environment Setup
1. Clone or download the project
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with the following variables:
   ```
   NEON_DATABASE_URL=your_neon_db_url
   QDRANT_CLUSTER_URL=your_qdrant_cluster_url
   QDRANT_API_KEY=your_qdrant_api_key
   COHERE_API_KEY=your_cohere_api_key
   OPENAI_API_KEY=your_openai_api_key
   SECRET_KEY=your_jwt_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

## Running the Application
1. Start the application: `uvicorn src.main:app --reload`
2. The API will be available at `http://localhost:8000`
3. API documentation available at `http://localhost:8000/docs`

## Core Workflow
1. **Ingest a book**: Use the POST `/ingest` endpoint to add a book to the system
2. **Query book content**: Use the POST `/query` endpoint for global questions
3. **Query specific sections**: Use POST `/query/section` for section-specific questions
4. **Query selected text**: Use POST `/query/selection` for questions about user-selected text

## Example Usage

### 1. Ingest a Book
```bash
curl -X POST "http://localhost:8000/v1/ingest" \
  -H "Authorization: Bearer your_jwt_token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Introduction to Machine Learning",
    "author": "AI Expert",
    "content": "Full book content here...",
    "metadata": {
      "publisher": "Tech Publishing"
    }
  }'
```

### 2. Ask a Global Question
```bash
curl -X POST "http://localhost:8000/v1/query" \
  -H "Authorization: Bearer your_jwt_token" \
  -H "Content-Type: application/json" \
  -d '{
    "book_id": "book-uuid-here",
    "question": "What are the main algorithms discussed in this book?"
  }'
```

### 3. Ask a Section-Specific Question
```bash
curl -X POST "http://localhost:8000/v1/query/section" \
  -H "Authorization: Bearer your_jwt_token" \
  -H "Content-Type: application/json" \
  -d '{
    "book_id": "book-uuid-here",
    "section_id": "section-uuid-here",
    "question": "Explain the concepts in this section?"
  }'
```

### 4. Ask About Selected Text
```bash
curl -X POST "http://localhost:8000/v1/query/selection" \
  -H "Authorization: Bearer your_jwt_token" \
  -H "Content-Type: application/json" \
  -d '{
    "book_id": "book-uuid-here",
    "selected_text": "The key concept is reinforcement learning...",
    "question": "What does reinforcement learning mean?"
  }'
```

## Architecture Overview
- **API Layer**: FastAPI handles HTTP requests and responses
- **Service Layer**: Contains business logic for ingestion, retrieval, and reasoning
- **Data Layer**: Neon Postgres stores structured data (books, chapters, users)
- **Vector Store**: Qdrant handles vector embeddings for similarity search
- **AI Layer**: OpenAI agents for response generation with Cohere embeddings

## Testing
Run the test suite: `pytest tests/`

- Unit tests: `pytest tests/unit/`
- Integration tests: `pytest tests/integration/`
- Contract tests: `pytest tests/contract/`
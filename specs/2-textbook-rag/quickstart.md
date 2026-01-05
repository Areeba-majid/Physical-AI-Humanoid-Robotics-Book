# Quickstart Guide: Physical AI & Humanoid Robotics Textbook with RAG Chatbot

## Overview
This guide provides instructions for setting up, running, and testing the Physical AI & Humanoid Robotics textbook with RAG chatbot system.

## Prerequisites
- Python 3.11+
- Node.js 18+
- Access to Qdrant Cloud (Free Tier)
- Access to Neon Serverless PostgreSQL
- API keys for required services

## Environment Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and configure environment files:
   ```bash
   # Backend environment
   cd backend
   cp .env.example .env
   # Edit .env with your specific configuration
   ```

3. Set up backend dependencies:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Set up frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Environment Variables
Create `.env` files in both backend and frontend directories with the following variables:

Backend (.env):
```env
DATABASE_URL=your_neon_postgres_connection_string
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
COHERE_API_KEY=your_cohere_api_key
OPENAI_API_KEY=your_openai_api_key_or_empty
RATE_LIMIT_REQUESTS=10
RATE_LIMIT_WINDOW=60
```

## Database Setup
1. Set up PostgreSQL tables:
   ```bash
   cd backend
   python -m src.core.database.setup
   ```

2. Import textbook content:
   ```bash
   cd backend
   python -m src.core.content.ingest
   ```

## Running the Application
1. Start the backend:
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

2. In a new terminal, start the frontend:
   ```bash
   cd frontend
   npm start
   ```

## API Testing
1. Test chapter retrieval:
   ```bash
   curl -X GET "http://localhost:8000/api/textbook/chapters"
   ```

2. Test RAG functionality:
   ```bash
   curl -X POST "http://localhost:8000/api/chatbot/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the main components of a humanoid robot?"}'
   ```

## Verification Steps
1. Navigate to the frontend (typically http://localhost:3000)
2. Verify all 6 textbook chapters are accessible
3. Test the RAG chatbot with questions from each chapter
4. Verify citations appear in responses
5. Test chapter-scoped questions
6. Verify rate limiting after 10 requests per minute per IP

## Common Issues
- If the RAG responses are empty, check that content was properly ingested into Qdrant
- If citations are missing, verify that the citation extraction process is working
- If rate limiting doesn't work, ensure the UserSession management is active

## Next Steps
- Review the detailed architecture in the plan.md document
- Examine the data models in data-model.md
- Check the API contracts in the contracts/ directory
- Explore the implementation tasks in tasks.md (to be generated)
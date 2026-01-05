# Quickstart Guide: AI-native Physical AI & Humanoid Robotics Textbook Platform

## Prerequisites

- Node.js 20.x or higher
- Python 3.11 or higher
- MongoDB 6.x or higher
- Git
- Docker (optional, for containerized deployment)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your configuration:
# - MONGODB_URI=your_mongodb_connection_string
# - QDRANT_URL=your_qdrant_cloud_url
# - GEMINI_API_KEY=your_gemini_api_key
# - BETTER_AUTH_SECRET=your_auth_secret
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Set environment variables
cp .env.example .env
# Edit .env with your configuration:
# - REACT_APP_API_URL=your_backend_url
# - REACT_APP_GEMINI_API_KEY=your_gemini_api_key
```

### 4. Initialize Database
```bash
# From backend directory
python -m src.main init_db
```

### 5. Load Textbook Content
```bash
# From project root
python scripts/load_content.py --source docs/textbook/
```

### 6. Run the Application

#### Development Mode:
```bash
# Terminal 1 - Start backend
cd backend
python -m uvicorn src.main:app --reload --port 8000

# Terminal 2 - Start frontend
cd frontend
npm start
```

#### Production Mode with Docker:
```bash
# Build and run containers
docker-compose up --build
```

## API Contracts

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login existing user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user info

### Textbook Content
- `GET /api/chapters` - List all chapters
- `GET /api/chapters/{id}` - Get specific chapter
- `GET /api/chapters/{id}/urdu` - Get Urdu translation of chapter

### Quiz System
- `GET /api/quizzes/{chapter_id}` - Get quiz for a chapter
- `POST /api/quizzes/{quiz_id}/submit` - Submit quiz answers
- `GET /api/quizzes/{quiz_id}/results` - Get quiz results

### Progress Tracking
- `GET /api/users/{id}/progress` - Get user progress
- `POST /api/users/{id}/progress` - Update user progress
- `GET /api/users/{id}/recommendations` - Get personalized recommendations

### Chatbot
- `POST /api/chat` - Send message to RAG chatbot
- `GET /api/chat/{session_id}` - Get chat history
- `POST /api/chat/{session_id}/feedback` - Submit chat feedback

## Configuration

### Environment Variables

#### Backend (.env):
- `MONGODB_URI` - Connection string for MongoDB
- `QDRANT_URL` - URL for Qdrant Cloud instance
- `QDRANT_API_KEY` - API key for Qdrant Cloud
- `GEMINI_API_KEY` - API key for Google Gemini
- `BETTER_AUTH_SECRET` - Secret for BetterAuth
- `BETTER_AUTH_URL` - Base URL for the application
- `DATABASE_NAME` - Name of the MongoDB database

#### Frontend (.env):
- `REACT_APP_API_URL` - Base URL for backend API
- `REACT_APP_GEMINI_API_KEY` - API key for Google Gemini (if needed client-side)
- `REACT_APP_SITE_URL` - Base URL for the frontend site

## Development

### Running Tests
```bash
# Backend tests
cd backend
python -m pytest tests/

# Frontend tests
cd frontend
npm test
```

### Building for Production
```bash
# Frontend build
cd frontend
npm run build

# Backend build (if using containers)
cd backend
docker build -t textbook-platform-backend .
```

### Adding Textbook Content
1. Add new markdown files to `docs/textbook/`
2. Run the content loading script: `python scripts/load_content.py --source docs/textbook/`
3. Update embeddings: `python scripts/update_embeddings.py`

## Troubleshooting

### Common Issues
1. **API requests timing out**: Check that MongoDB and Qdrant connections are properly configured
2. **Chatbot not responding**: Verify GEMINI_API_KEY is properly set and has sufficient quota
3. **Urdu text not rendering correctly**: Ensure Noto Nastaliq Urdu font is properly loaded
4. **Slow page loading**: Consider enabling caching and optimizing database queries

### Useful Commands
```bash
# Check backend health
curl http://localhost:8000/health

# Check all environment variables are set
cd backend && python -c "import os; print([k for k in os.environ.keys() if 'API_KEY' in k or 'URI' in k or 'SECRET' in k])"

# Reset database (⚠️ This will delete all data)
cd backend && python -m src.main reset_db
```
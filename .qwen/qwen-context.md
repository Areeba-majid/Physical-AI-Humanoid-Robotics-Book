# AI-native Robotics Textbook Platform Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-16

## Active Technologies

- Python 3.11
- FastAPI
- Docusaurus
- React
- TypeScript 5.x
- Tailwind CSS
- MongoDB
- Qdrant Cloud
- Google Gemini 2.5 Flash
- BetterAuth
- Node.js 20.x

## Project Structure

```text
backend/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   ├── chapter.py
│   │   ├── quiz.py
│   │   ├── progress.py
│   │   ├── recommendation.py
│   │   └── chat_interaction.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── rag_service.py
│   │   ├── translation_service.py
│   │   ├── quiz_service.py
│   │   └── personalization_service.py
│   ├── api/
│   │   ├── auth_router.py
│   │   ├── textbook_router.py
│   │   ├── chat_router.py
│   │   ├── quiz_router.py
│   │   └── user_router.py
│   ├── utils/
│   │   ├── embedding_utils.py
│   │   ├── text_processing.py
│   │   └── translation_utils.py
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
└── requirements.txt

frontend/
├── docusaurus.config.js
├── package.json
├── src/
│   ├── components/
│   │   ├── ChatBot/
│   │   ├── Quiz/
│   │   ├── Dashboard/
│   │   ├── TranslationToggle/
│   │   ├── ThemeToggle/
│   │   └── TextHighlighter/
│   ├── pages/
│   ├── css/
│   ├── utils/
│   └── theme/
├── static/
├── i18n/
│   └── ur/
│       └── docusaurus-theme-classic/
│           └── navbar.json
├── babel.config.js
└── tailwind.config.js

scripts/
├── setup.sh
└── deploy.sh

docs/
└── textbook/
    ├── intro.md
    ├── chapter1.md
    └── ...

specs/1-ai-textbook-platform/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── api-contract.md
└── tasks.md
```

## Commands

### Backend Commands
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
uvicorn src.main:app --reload --port 8000

# Run tests
python -m pytest tests/

# Initialize database
python -m src.main init_db
```

### Frontend Commands
```bash
# Install dependencies
npm install

# Run development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

### Docker Commands
```bash
# Build and run containers
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

## Code Style

### Python
- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Use docstrings for all public methods and classes
- Use async/await for I/O-bound operations

### TypeScript/React
- Use functional components with hooks
- Use TypeScript interfaces for all props and state
- Follow React best practices for component composition
- Use Tailwind CSS utility classes for styling

### Database Models
- Use Pydantic models for request/response validation
- Define clear relationships between entities
- Include proper validation rules
- Add appropriate indexes for performance

## Recent Changes

- **Feature 1**: Implemented core textbook platform with multi-chapter navigation, RAG chatbot with citations, Urdu translation with RTL support, personalized dashboard, and AI-generated quizzes
  - Added data models for User, Chapter, Quiz, Progress, Recommendation, ChatInteraction, and Translation
  - Set up API contracts for authentication, textbook content, quizzes, progress tracking, and chatbot
  - Configured backend with FastAPI and frontend with Docusaurus/React
  - Implemented sentence-aware text chunking to preserve context during RAG processing
  - Added WCAG AA accessibility compliance features

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
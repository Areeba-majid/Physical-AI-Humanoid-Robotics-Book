# API Contract: Textbook Platform

## Base URL
`https://api.textbook-platform.example.com`

## Authentication
All endpoints require authentication via JWT token in the Authorization header:
`Authorization: Bearer {token}`

## Content Types
- Requests: `application/json`
- Responses: `application/json` unless otherwise specified

---

## User Management

### Register User
`POST /api/auth/register`

**Description**: Register a new user account

**Request Body**:
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securePassword123",
  "fullName": "John Doe"
}
```

**Responses**:
- `201 Created`: User successfully registered
- `400 Bad Request`: Invalid input data
- `409 Conflict`: Email or username already exists

### Login User
`POST /api/auth/login`

**Description**: Authenticate user and return JWT token

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response**:
```json
{
  "token": "jwt-token-string",
  "user": {
    "id": "user-id",
    "email": "user@example.com",
    "username": "johndoe",
    "fullName": "John Doe"
  }
}
```

**Responses**:
- `200 OK`: Authentication successful
- `401 Unauthorized`: Invalid credentials

### Get Current User
`GET /api/auth/me`

**Description**: Get information about the authenticated user

**Response**:
```json
{
  "id": "user-id",
  "email": "user@example.com",
  "username": "johndoe",
  "fullName": "John Doe",
  "preferences": {
    "language": "en",
    "theme": "light"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "lastLoginAt": "2023-01-02T10:30:00Z"
}
```

---

## Textbook Content

### List All Chapters
`GET /api/chapters`

**Description**: Retrieve a list of all available textbook chapters

**Query Parameters**:
- `language` (optional): Language code (e.g., "en", "ur") - defaults to "en"
- `limit` (optional): Number of results to return (max 50)
- `offset` (optional): Number of results to skip

**Response**:
```json
{
  "chapters": [
    {
      "id": "chapter-1",
      "title": "Introduction to AI",
      "orderIndex": 1,
      "wordCount": 1500,
      "readingTimeEstimate": 7,
      "status": "published"
    }
  ],
  "total": 12,
  "limit": 10,
  "offset": 0
}
```

### Get Specific Chapter
`GET /api/chapters/{id}`

**Description**: Retrieve a specific chapter by ID

**Path Parameters**:
- `id`: Chapter ID

**Query Parameters**:
- `language` (optional): Language code (e.g., "en", "ur") - defaults to "en"

**Response**:
```json
{
  "id": "chapter-1",
  "title": "Introduction to AI",
  "content": "Full chapter content as markdown or HTML",
  "sections": [
    {
      "title": "What is AI?",
      "content": "Section content..."
    }
  ],
  "orderIndex": 1,
  "wordCount": 1500,
  "readingTimeEstimate": 7,
  "associatedQuizId": "quiz-1",
  "status": "published",
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-02T15:30:00Z"
}
```

### Get Chapter in Urdu
`GET /api/chapters/{id}/urdu`

**Description**: Retrieve the Urdu translation of a chapter

**Path Parameters**:
- `id`: Chapter ID

**Response**:
```json
{
  "id": "chapter-1",
  "title": "مصنوعی ذہانت کا تعارف",
  "content": " Urdu chapter content",
  "orderIndex": 1,
  "status": "published"
}
```

---

## Quiz System

### Get Quiz for Chapter
`GET /api/quizzes/{chapterId}`

**Description**: Retrieve the quiz associated with a chapter

**Path Parameters**:
- `chapterId`: ID of the chapter

**Response**:
```json
{
  "id": "quiz-1",
  "title": "Chapter 1 Quiz",
  "chapterId": "chapter-1",
  "questions": [
    {
      "id": "q1",
      "questionText": "What is AI?",
      "questionType": "mcq",
      "options": [
        "Artificial Intelligence",
        "Automated Interface",
        "Advanced Integration",
        "None of the above"
      ],
      "correctAnswer": "Artificial Intelligence",
      "explanation": "AI stands for Artificial Intelligence..."
    }
  ],
  "totalPoints": 10,
  "difficulty": "beginner",
  "timeLimit": null
}
```

### Submit Quiz Answers
`POST /api/quizzes/{quizId}/submit`

**Description**: Submit answers for a quiz

**Path Parameters**:
- `quizId`: ID of the quiz

**Request Body**:
```json
{
  "answers": [
    {
      "questionId": "q1",
      "selectedOption": "Artificial Intelligence"
    }
  ]
}
```

**Response**:
```json
{
  "quizId": "quiz-1",
  "userId": "user-id",
  "score": 8,
  "maxScore": 10,
  "percentage": 80,
  "feedback": [
    {
      "questionId": "q1",
      "isCorrect": true,
      "correctAnswer": "Artificial Intelligence",
      "explanation": "AI stands for Artificial Intelligence..."
    }
  ]
}
```

---

## Progress Tracking

### Get User Progress
`GET /api/users/{userId}/progress`

**Description**: Retrieve the learning progress for a user

**Path Parameters**:
- `userId`: ID of the user

**Query Parameters**:
- `chapterId` (optional): Filter by specific chapter

**Response**:
```json
{
  "userId": "user-id",
  "progress": [
    {
      "id": "progress-1",
      "chapterId": "chapter-1",
      "quizId": "quiz-1",
      "status": "completed",
      "currentPosition": 1500,
      "timeSpentSeconds": 420,
      "quizScore": 8,
      "quizCompletedAt": "2023-01-02T12:00:00Z",
      "startedAt": "2023-01-02T11:30:00Z",
      "completedAt": "2023-01-02T12:00:00Z",
      "notes": "Found this chapter challenging"
    }
  ]
}
```

### Update User Progress
`POST /api/users/{userId}/progress`

**Description**: Update the learning progress for a user

**Path Parameters**:
- `userId`: ID of the user

**Request Body**:
```json
{
  "chapterId": "chapter-1",
  "status": "in_progress",
  "currentPosition": 750,
  "timeSpentSeconds": 210,
  "notes": "Good introduction to concepts"
}
```

**Response**:
```json
{
  "id": "progress-1",
  "userId": "user-id",
  "chapterId": "chapter-1",
  "status": "in_progress",
  "currentPosition": 750,
  "timeSpentSeconds": 210,
  "notes": "Good introduction to concepts",
  "updatedAt": "2023-01-02T11:45:00Z"
}
```

### Get User Recommendations
`GET /api/users/{userId}/recommendations`

**Description**: Retrieve personalized content recommendations for a user

**Path Parameters**:
- `userId`: ID of the user

**Response**:
```json
{
  "userId": "user-id",
  "recommendations": [
    {
      "id": "rec-1",
      "itemId": "chapter-3",
      "itemType": "chapter",
      "title": "Machine Learning Fundamentals",
      "reason": "Based on your progress in Chapter 1",
      "priority": 4,
      "viewedAt": null
    }
  ]
}
```

---

## Chatbot

### Send Message to Chatbot
`POST /api/chat`

**Description**: Send a message to the RAG chatbot and receive a response

**Request Body**:
```json
{
  "message": "What is the definition of machine learning?",
  "sessionId": "session-123",  // Optional, creates new session if not provided
  "context": {  // Optional, additional context for the query
    "chapterId": "chapter-2",
    "sectionTitle": "Supervised Learning"
  }
}
```

**Response**:
```json
{
  "id": "interaction-1",
  "sessionId": "session-123",
  "userMessage": "What is the definition of machine learning?",
  "aiResponse": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
  "citations": [
    {
      "source": "Chapter 2: Machine Learning Fundamentals",
      "snippet": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed...",
      "link": "/chapters/2#definition"
    }
  ],
  "timestamp": "2023-01-02T10:30:00Z"
}
```

### Get Chat History
`GET /api/chat/{sessionId}`

**Description**: Retrieve chat history for a session

**Path Parameters**:
- `sessionId`: ID of the chat session

**Response**:
```json
{
  "sessionId": "session-123",
  "messages": [
    {
      "id": "interaction-1",
      "userMessage": "What is the definition of machine learning?",
      "aiResponse": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
      "citations": [...],
      "timestamp": "2023-01-02T10:30:00Z"
    }
  ]
}
```
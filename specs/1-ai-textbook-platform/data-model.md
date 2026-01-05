# Data Model: AI-native Physical AI & Humanoid Robotics Textbook Platform

## Entity Models

### User
Represents a registered learner with profile, authentication data, preferences, and learning metadata.

```python
class User:
    id: str (primary key)
    email: str (required, unique, valid email format)
    username: str (required, unique)
    password_hash: str (required, for authentication)
    full_name: str (optional)
    preferences: dict (optional, e.g., {"language": "en", "theme": "light"})
    created_at: datetime (required)
    updated_at: datetime (required)
    last_login_at: datetime (optional)
    is_verified: bool (default: false)
    profile_image_url: str (optional)
```

### Chapter
Represents textbook content with multiple sections, text content, and associated quizzes/summaries.

```python
class Chapter:
    id: str (primary key)
    title: str (required)
    content: str (required, the main text content)
    content_ur: str (optional, Urdu translation)
    sections: list[dict] (optional, structured sections)
    order_index: int (required, for navigation)
    created_at: datetime (required)
    updated_at: datetime (required)
    word_count: int (optional, for progress tracking)
    reading_time_estimate: int (optional, in minutes)
    associated_quiz_id: str (optional, foreign key)
    status: str (required, e.g., "published", "draft")
    metadata: dict (optional, extra information)
```

### Quiz
Represents assessment questions (MCQs and short answers) generated from chapter content.

```python
class Quiz:
    id: str (primary key)
    title: str (required)
    chapter_id: str (required, foreign key)
    questions: list[dict] 
        - question_text: str (required)
        - question_type: str (required, e.g., "mcq", "short_answer")
        - options: list[str] (required for MCQs)
        - correct_answer: str (required)
        - explanation: str (optional, for feedback)
    created_at: datetime (required)
    updated_at: datetime (required)
    time_limit: int (optional, in seconds)
    total_points: int (required)
    difficulty: str (required, e.g., "beginner", "intermediate", "advanced")
```

### Progress
Represents user's learning status, including completed chapters, quiz scores, and time spent.

```python
class Progress:
    id: str (primary key)
    user_id: str (required, foreign key)
    chapter_id: str (required, foreign key)
    quiz_id: str (optional, foreign key)
    status: str (required, e.g., "not_started", "in_progress", "completed")
    current_position: int (optional, for tracking reading position)
    time_spent_seconds: int (required, total time spent on content)
    quiz_score: int (optional, score for completed quiz)
    quiz_completed_at: datetime (optional)
    started_at: datetime (required)
    completed_at: datetime (optional)
    notes: str (optional, user's personal notes)
```

### Recommendation
Represents personalized content suggestions based on user profile and progress.

```python
class Recommendation:
    id: str (primary key)
    user_id: str (required, foreign key)
    item_id: str (required, ID of recommended item)
    item_type: str (required, e.g., "chapter", "quiz", "resource")
    reason: str (required, explanation for recommendation)
    priority: int (required, 1-5 scale)
    created_at: datetime (required)
    viewed_at: datetime (optional)
    clicked_at: datetime (optional)
```

### ChatInteraction
Represents a conversation between user and RAG chatbot with citations.

```python
class ChatInteraction:
    id: str (primary key)
    user_id: str (required, foreign key)
    session_id: str (required, to group related conversations)
    user_message: str (required)
    ai_response: str (required)
    citations: list[dict] 
        - source: str (required, e.g., chapter title, page)
        - snippet: str (required, text snippet)
        - link: str (optional, link to source)
    created_at: datetime (required)
    context_used: str (optional, text used for RAG context)
    feedback_rating: int (optional, 1-5 scale)
    feedback_comment: str (optional)
```

### Translation
Represents language-specific versions of textbook content with RTL layout support.

```python
class Translation:
    id: str (primary key)
    original_content_id: str (required, foreign key to chapter/text)
    original_language: str (required, e.g., "en")
    target_language: str (required, e.g., "ur")
    translated_content: str (required)
    translator: str (optional, who translated)
    status: str (required, e.g., "pending", "approved", "in_review")
    created_at: datetime (required)
    updated_at: datetime (required)
    approval_status: str (required, e.g., "pending", "approved", "rejected")
    approved_by: str (optional, user who approved)
    approval_date: datetime (optional)
```

## Validation Rules from Requirements

### User Model
- Email must be unique and follow valid email format
- Username must be unique
- Password must meet security requirements (min 8 chars, etc.)
- User preferences must be a valid JSON object

### Chapter Model
- Title and content must not be empty
- order_index must be unique within a textbook
- Content and content_ur (if provided) must be properly formatted
- Status must be either "published" or "draft"

### Quiz Model
- Questions must have at least one option for MCQs
- Correct answer must be one of the provided options for MCQs
- Total points must be >= 0
- Difficulty must be one of the allowed values

### Progress Model
- status must be one of: "not_started", "in_progress", "completed"
- quiz_score must be <= total_points if quiz_id is provided
- user_id and chapter_id combination must be unique for the same chapter

### Recommendation Model
- priority must be between 1 and 5 inclusive
- item_type must be one of: "chapter", "quiz", "resource"

### ChatInteraction Model
- feedback_rating must be between 1 and 5 inclusive
- Created_at timestamp must be set automatically

### Translation Model
- original_language and target_language must be different
- approval_status must be one of: "pending", "approved", "rejected"
- Target language must be currently supported by the system

## Relationships

- User → Progress (one-to-many)
- Chapter → Progress (one-to-many)
- Chapter → Quiz (one-to-one, optional)
- User → ChatInteraction (one-to-many)
- User → Recommendation (one-to-many)
- Chapter → Translation (one-to-many, optional)
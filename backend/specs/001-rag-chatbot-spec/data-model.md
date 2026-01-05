# Data Model: Integrated RAG Chatbot Development

**Feature**: 001-rag-chatbot-spec
**Date**: 2025-12-17

## Overview
This document defines the data model for the RAG chatbot system, outlining the entities, their attributes, relationships, and validation rules as required by the feature specification.

## Entity: Book
Represents a book that has been ingested into the system.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the book
- `title`: String (Required, Max 500 chars) - Title of the book
- `author`: String (Required, Max 200 chars) - Author of the book
- `isbn`: String (Optional, Max 17 chars) - ISBN identifier for the book
- `content`: Text (Required) - Full text content of the book
- `created_at`: DateTime (Auto-generated) - Timestamp of book creation
- `updated_at`: DateTime (Auto-generated) - Timestamp of last update
- `metadata`: JSON (Optional) - Additional metadata about the book

### Validation Rules
- Title must be non-empty
- Author must be non-empty
- ISBN, if provided, must follow proper format (10 or 13 digits with optional hyphens)
- Content must not be empty

### Relationships
- One-to-Many with Chapter (one book has many chapters)
- Many-to-Many with User through UserBookAccess (many users can access many books)

## Entity: Chapter
Represents a chapter within a book.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the chapter
- `book_id`: UUID (Foreign Key) - Reference to the parent book
- `title`: String (Required, Max 300 chars) - Title of the chapter
- `content`: Text (Required) - Text content of the chapter
- `chapter_number`: Integer (Required) - Sequential number of the chapter in the book
- `page_start`: Integer (Optional) - Starting page number of the chapter
- `page_end`: Integer (Optional) - Ending page number of the chapter
- `created_at`: DateTime (Auto-generated) - Timestamp of chapter creation
- `updated_at`: DateTime (Auto-generated) - Timestamp of last update

### Validation Rules
- Title must be non-empty
- Content must not be empty
- Chapter number must be positive
- Page numbers, if provided, must be positive and start < end

### Relationships
- Many-to-One with Book (many chapters belong to one book)
- One-to-Many with Section (one chapter has many sections)

## Entity: Section
Represents a subsection within a chapter.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the section
- `chapter_id`: UUID (Foreign Key) - Reference to the parent chapter
- `title`: String (Optional, Max 300 chars) - Title of the section
- `content`: Text (Required) - Text content of the section
- `section_number`: Integer (Optional) - Sequential number of the section in the chapter
- `start_position`: Integer (Required) - Character position where the section starts in the chapter
- `end_position`: Integer (Required) - Character position where the section ends in the chapter
- `created_at`: DateTime (Auto-generated) - Timestamp of section creation
- `updated_at`: DateTime (Auto-generated) - Timestamp of last update

### Validation Rules
- Content must not be empty
- Start position must be less than end position
- Start and end positions must be within the bounds of the parent chapter's content
- Section number, if provided, must be positive

### Relationships
- Many-to-One with Chapter (many sections belong to one chapter)

## Entity: User
Represents a user of the system.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the user
- `username`: String (Required, Max 100 chars, Unique) - User's unique username
- `email`: String (Required, Max 255 chars, Unique) - User's email address
- `full_name`: String (Optional, Max 200 chars) - User's full name
- `hashed_password`: String (Required) - Hashed password for authentication
- `is_active`: Boolean (Default: true) - Whether the account is active
- `role`: String (Enum: user, admin) - User's role in the system
- `created_at`: DateTime (Auto-generated) - Timestamp of user creation
- `updated_at`: DateTime (Auto-generated) - Timestamp of last update

### Validation Rules
- Username must be unique and non-empty
- Email must be valid and unique
- Password must meet security requirements
- Role must be one of the allowed values

### Relationships
- Many-to-Many with Book through UserBookAccess (many users can access many books)
- One-to-Many with QueryLog (one user can make many queries)

## Entity: UserBookAccess
Junction table for the many-to-many relationship between users and books.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the access record
- `user_id`: UUID (Foreign Key) - Reference to the user
- `book_id`: UUID (Foreign Key) - Reference to the book
- `access_level`: String (Enum: read, contribute) - Level of access granted
- `granted_at`: DateTime (Auto-generated) - Timestamp when access was granted
- `revoked_at`: DateTime (Optional) - Timestamp when access was revoked

### Validation Rules
- User and book combination must be unique when active
- Access level must be one of the allowed values

### Relationships
- Many-to-One with User
- Many-to-One with Book

## Entity: QueryLog
Records queries made by users for analytics and debugging.

### Attributes
- `id`: UUID (Primary Key) - Unique identifier for the log entry
- `user_id`: UUID (Foreign Key) - Reference to the user who made the query
- `book_id`: UUID (Foreign Key) - Reference to the book queried
- `query_text`: Text (Required) - The text of the user's query
- `query_mode`: String (Enum: global, section, selection) - The mode of the query
- `section_id`: UUID (Optional, Foreign Key) - Reference to section if section-scoped query
- `selected_text`: Text (Optional) - The user-selected text if in selection mode
- `response_text`: Text (Required) - The system's response to the query
- `query_timestamp`: DateTime (Auto-generated) - When the query was made
- `response_tokens`: Integer (Optional) - Number of tokens in the response
- `processing_time`: Float (Optional) - Time taken to process the query in seconds

### Validation Rules
- Query and response text must not be empty
- Query mode must be one of the allowed values
- If query mode is 'section', section_id must be provided
- If query mode is 'selection', selected_text must be provided

### Relationships
- Many-to-One with User
- Many-to-One with Book
- Many-to-One with Section (optional, for section-scoped queries)

## Vector Embedding (Stored in Qdrant, not Postgres)
Represents vector embeddings of text chunks for similarity search.

### Attributes
- `id`: UUID - Unique identifier for the embedding
- `book_id`: UUID - Reference to the associated book
- `chapter_id`: UUID - Reference to the associated chapter
- `section_id`: UUID - Reference to the associated section (optional)
- `content`: Text - The original text that was embedded
- `embedding`: Array of Floats - The vector representation of the content
- `metadata`: JSON - Additional metadata for filtering (book_id, chapter_id, section_id)

### Relationships
- The relationships are maintained through metadata rather than foreign keys due to the nature of vector databases
- Maps to Book, Chapter, and Section through metadata fields
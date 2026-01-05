# Research Summary: AI-native Physical AI & Humanoid Robotics Textbook Platform

## Overview
This document summarizes research conducted to resolve technical unknowns and make informed decisions for the AI-native textbook platform implementation.

## Technology Decisions

### Backend Framework: FastAPI
- **Decision**: Use FastAPI for the backend API
- **Rationale**: FastAPI offers excellent performance, built-in async support, automatic API documentation (Swagger UI), and strong typing with Pydantic. It's well-suited for ML/AI integrations and supports the required performance goals.
- **Alternatives considered**: Flask, Django, Node.js with Express
- **Reference**: Spec requirement mentions "Backend Stack: - FastAPI with proper REST endpoints"

### Frontend Framework: Docusaurus + React
- **Decision**: Use Docusaurus as the documentation/content framework with React for interactive components
- **Rationale**: Docusaurus is specifically designed for documentation sites, supports multi-language content, and integrates well with React components. It supports the required Urdu RTL layout and offers excellent SEO capabilities.
- **Alternatives considered**: Next.js, Gatsby, VuePress
- **Reference**: Spec requirement mentions "Frontend Stack: - Docusaurus for textbook content"

### Database: MongoDB + Qdrant Cloud
- **Decision**: Use MongoDB for application data and Qdrant Cloud for embeddings
- **Rationale**: MongoDB offers flexible schema for user profiles and content metadata. Qdrant is a purpose-built vector database optimized for similarity search required by the RAG system.
- **Alternatives considered**: PostgreSQL with pgvector, Pinecone, Weaviate
- **Reference**: Spec requirement mentions "MongoDB for user profiles, progress, translation jobs, and quizzes" and "Qdrant Cloud for embeddings and RAG retrieval"

### Authentication: BetterAuth
- **Decision**: Implement BetterAuth for user authentication
- **Rationale**: BetterAuth is a modern authentication library that provides secure, customizable authentication with support for various providers. It's lightweight and integrates well with TypeScript/React applications.
- **Alternatives considered**: Auth0, Firebase Auth, NextAuth.js, Supabase Auth
- **Reference**: Spec requirement mentions "Authentication system (signup/login) and BetterAuth bonus"

### AI Integration: Google Gemini 2.5 Flash
- **Decision**: Use Google's Gemini 2.5 Flash for AI-powered features
- **Rationale**: Gemini 2.5 Flash provides excellent performance for text generation with low latency, which is important for the <2 second chatbot response time requirement. It supports the RAG functionality with citation support.
- **Alternatives considered**: OpenAI GPT models, Anthropic Claude, Mistral, Ollama
- **Reference**: Spec requirement mentions "Gemini 2.5 Flash for AI generation (summaries, quiz, chatbot)"

### Text Processing: Sentence-Aware Chunking
- **Decision**: Implement sentence-aware text chunking for the RAG system
- **Rationale**: To prevent breaking sentences during "very long chapters → chunk without breaking sentences" as specified in the edge cases. This ensures proper context for the AI model and maintains text coherence.
- **Alternatives considered**: Fixed-size chunking, paragraph-based chunking
- **Reference**: Spec requirement mentions "Very long chapters → chunk without breaking sentences"

### Urdu Translation Implementation
- **Decision**: Use CSS RTL support and Noto Nastaliq Urdu font for Urdu translation
- **Rationale**: CSS provides native RTL layout support. Noto Nastaliq Urdu is specifically designed for proper rendering of Urdu script. Code blocks will be preserved as-is as specified in edge cases.
- **Alternatives considered**: Custom RTL implementation vs. CSS RTL support
- **Reference**: Spec requirement mentions "Urdu translation: RTL layout, text alignment correct, proper font for Urdu (Noto Nastaliq or similar)" and "Urdu translation of code blocks → skip code translation"

### Caching Strategy
- **Decision**: Implement Redis for caching frequently accessed data
- **Rationale**: To meet performance requirements of <2 seconds load times and support 100+ concurrent users. Redis provides fast in-memory caching for user sessions, frequently accessed chapters, and AI model responses.
- **Alternatives considered**: In-memory caching, database-level caching
- **Reference**: Spec requirement for performance "Load in < 2 seconds on broadband", "Chatbot latency < 2 seconds", "Support ≥100 concurrent users"

### Monitoring and Analytics
- **Decision**: Implement logging and metrics collection for compliance with WCAG AA standards and performance monitoring
- **Rationale**: To ensure WCAG AA compliance is maintained and to monitor response times and user interactions for accessibility issues.
- **Alternatives considered**: Third-party analytics vs. custom logging
- **Reference**: Spec requirement for "WCAG AA accessibility compliance"

### Deployment Architecture
- **Decision**: Containerized microservices architecture with separate services for frontend, backend, database, and vector store
- **Rationale**: Enables independent scaling and maintenance of components. Supports the hackathon requirement for clean repo structure and working deployment.
- **Alternatives considered**: Monolithic deployment, serverless functions
- **Reference**: Spec requirement for "Clean, responsive, modern frontend + backend" and "Clean GitHub repo structure"
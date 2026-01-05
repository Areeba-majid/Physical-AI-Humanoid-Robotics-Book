# Research: Physical AI & Humanoid Robotics Textbook with RAG Chatbot

## Overview
This document captures research findings and decisions for implementing the Physical AI & Humanoid Robotics textbook with RAG chatbot.

## Decision: Tech Stack Selection
**Decision**: Use FastAPI + Docusaurus + Qdrant Cloud + PostgreSQL Neon
**Rationale**: 
- FastAPI provides excellent performance for RAG operations with good async support
- Docusaurus is ideal for documentation-heavy sites like textbooks
- Qdrant Cloud provides managed vector storage with good Python integration
- PostgreSQL Neon provides serverless PostgreSQL with good performance characteristics

**Alternatives considered**:
- Backend: Flask vs. FastAPI - FastAPI chosen for better async support and performance
- Frontend: Next.js vs. Docusaurus - Docusaurus chosen for its documentation features
- Vector DB: Pinecone vs. Qdrant vs. Weaviate - Qdrant chosen for better open-source support and cost
- RDBMS: Supabase vs. Neon - Neon chosen for better PostgreSQL compatibility

## Decision: Embedding Model
**Decision**: Use sentence-transformers/all-MiniLM-L6-v2
**Rationale**: 
- Good balance of performance and accuracy
- CPU-friendly model as required by spec
- Smaller size means faster processing
- Well-established model with good community support

**Alternatives considered**:
- all-mpnet-base-v2: More accurate but slower and larger
- all-distilroberta-v1: Slower despite being distilled
- Instructor Embedding: More complex, not needed for this use case

## Decision: Citation Strategy
**Decision**: Implement chapter and section citations in RAG responses
**Rationale**: 
- Required by constitution for academic integrity
- Provides user with source verification capability
- Enables navigation to referenced content
- Maintains trust in the system

**Implementation**: Extract chapter and section information during ingestion, include in metadata, and surface in responses

## Decision: Rate Limiting Implementation
**Decision**: Implement per-IP rate limiting of 10 requests/minute
**Rationale**: 
- Required by functional requirement FR-006
- Protects backend resources from overuse
- Simple to implement and maintain
- Fair to all users

**Implementation**: Use FastAPI middleware with in-memory store or Redis for distributed deployments

## Decision: Error Handling
**Decision**: Return "The textbook does not contain enough information to answer this question" for insufficient context
**Rationale**: 
- Required by the functional requirement and constitution
- Prevents hallucination
- Maintains academic integrity
- Provides clear feedback to users

**Implementation**: Check similarity scores during RAG retrieval and return appropriate message if below threshold

## Decision: UI Design
**Decision**: Implement using the specified color palette (#F8F3D9, #EBE5C2, #B9B28A, #504B38)
**Rationale**: 
- Required by project constraints
- Provides consistent, academic-focused aesthetic
- Maintains visual coherence across application
- Professional appearance for textbook content

**Implementation**: Define CSS custom properties and Docusaurus theme customization

## Decision: Deployment Strategy
**Decision**: Deploy frontend to GitHub Pages, backend to Railway/Render
**Rationale**: 
- Meets free-tier requirements
- Good performance for the target use case
- Cost-effective for development and prototyping
- Good integration with existing workflows

**Implementation**: GitHub Actions for frontend, appropriate platform for backend deployment
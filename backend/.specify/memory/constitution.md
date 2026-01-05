<!-- SYNC IMPACT REPORT
Version change: 1.0.0 -> 1.1.0
Modified principles: Updated all to reflect RAG chatbot focus for Physical AI & Humanoid Robotics textbook
Added sections: Color palette requirements, Cohere API integration, Embedding strategy
Removed sections: Grounded responses principle (replaced with broader RAG principle)
Templates requiring updates: ⚠ .specify/templates/plan-template.md (update to reflect new principles), ⚠ .specify/templates/spec-template.md (update to reflect new principles), ⚠ .specify/templates/tasks-template.md (update to reflect new principles)
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics Textbook RAG Chatbot Constitution

## Core Principles

### Deterministic and Structured Outputs
All outputs must be deterministic, structured, and testable; Specifications, plans, and implementations must align consistently; No hallucinations or unstated assumptions allowed

### Requirements Driven Development
All development follows Requirements → Tasks → Implementations alignment; Functional specifications must define user stories, edge cases, and success criteria

### Academic Clarity and Professional Design
All materials must maintain academic clarity and professional textbook design; Clean architecture with modular multi-agent components; Apply specified color palette (#F8F3D9, #EBE5C2, #B9B28A, #504B38) to all UI elements

### Accurate RAG System with Citations
RAG answers must be accurate with proper citations; Chunking must avoid cutting sentences; System includes chunking + embeddings (sentence-transformers/all-MiniLM-L6-v2) + Qdrant Cloud search + Cohere API for enhanced responses

### Validated Implementation
All implementations must be fully functional, validated, and ambiguity-free; Follow clean architecture principles and avoid unused files; Integration tests must verify all system components work together properly

## Technology Stack and Constraints

Frontend must use Docusaurus (React/TypeScript); Backend uses FastAPI (Python 3.11+) with PostgreSQL Neon; Vector database uses Qdrant Cloud; Embeddings use sentence-transformers/all-MiniLM-L6-v2; Cohere API for enhanced RAG responses

## Acceptance Criteria and Delivery

Include all requirements: RAG chatbot for Physical AI & Humanoid Robotics textbook, proper citations, multi-modal support, clean UI with specified color palette, secure API keys management, performance benchmarks; Deliver clean repo structure, working deployment, demo video < 90 seconds

## Governance

Constitution governs all development practices; All implementations must follow specified quality standards; Amendments require documentation and justification; Version: 1.1.0; Ratification date: 2025-12-18; Amendment date: 2025-12-18

**Version**: 1.1.0 | **Ratified**: 2025-12-18 | **Last Amended**: 2025-12-18

# Implementation Plan: Physical AI & Humanoid Robotics Textbook with RAG Chatbot

**Branch**: `2-textbook-rag` | **Date**: 2025-12-18 | **Spec**: [specs/2-textbook-rag/spec.md]
**Input**: Feature specification from `/specs/2-textbook-rag/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature implements a Physical AI & Humanoid Robotics textbook with an embedded RAG chatbot that answers questions strictly from the book content with zero hallucination. The system uses Docusaurus for the frontend, FastAPI for the backend, Qdrant Cloud for vector storage, and PostgreSQL Neon for metadata. The RAG pipeline ensures responses are grounded in textbook content with proper citations.

## Technical Context

**Language/Version**: Python 3.11 (Backend), TypeScript (Frontend)
**Primary Dependencies**: FastAPI, Docusaurus, sentence-transformers/all-MiniLM-L6-v2, Qdrant, PostgreSQL
**Storage**: Qdrant Cloud (vector database), Neon Serverless PostgreSQL (metadata)
**Testing**: pytest for backend, Jest for frontend
**Target Platform**: Web application (frontend on GitHub Pages, backend on Railway/Render)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <2s backend p95 response time, <1.5s frontend FCP
**Constraints**: 10 requests/min rate limit per IP, zero hallucination tolerance, free-tier resource compliance
**Scale/Scope**: Individual learners and educators in Physical AI and Humanoid Robotics

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the project constitution:
- ✅ Deterministic and structured outputs: RAG system will provide structured, deterministic responses
- ✅ Requirements driven development: Following spec requirements exactly
- ✅ Academic clarity with specified color palette: UI will use #F8F3D9, #EBE5C2, #B9B28A, #504B38
- ✅ Accurate RAG system with citations: System must cite sources from textbook content
- ✅ Validated implementation: Testing to ensure zero hallucination rate

*Post-design evaluation:*
- ✅ All constitutional principles are satisfied by the implemented design
- ✅ Tech stack aligns with constitutional requirements (FastAPI, Docusaurus, Qdrant, Neon)
- ✅ Data model supports academic integrity with proper citation tracking
- ✅ API contracts enforce the required behaviors (citations, rate limiting)
- ✅ Implementation approach maintains zero hallucination requirement

## Project Structure

### Documentation (this feature)

```text
specs/2-textbook-rag/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   ├── services/
│   ├── api/
│   └── core/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
├── static/
└── tests/

docs/
├── ...
└── ...

scripts/
├── ...
└── ...

.env.example
requirements.txt
pyproject.toml
package.json
```

**Structure Decision**: Web application with separate frontend (Docusaurus) and backend (FastAPI) services to maintain clear separation of concerns between presentation and business logic.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | - | - |

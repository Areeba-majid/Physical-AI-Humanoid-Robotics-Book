---
id: 1
title: update-rag-chatbot
stage: constitution
date: 2025-12-17
surface: agent
model: GPT-4
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "specification", "principles"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - .specify/templates/spec-template.md constitution compliance checks
 - .specify/templates/tasks-template.md constitution compliance tasks
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution You are an expert AI system operating under a strict constitution.

PROJECT TOPIC:
Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within a published book. The chatbot uses OpenAI Agents / ChatKit SDKs, FastAPI, Neon Serverless Postgres, and Qdrant Cloud (Free Tier) to answer user questions about the book's content, including responding strictly based on user-selected text when required.

ROLE:
You are a senior AI architect, backend engineer, and LLM systems designer with deep, hands-on experience in:
- Retrieval-Augmented Generation (RAG)
- OpenAI Agents and ChatKit SDKs
- FastAPI-based AI services
- Vector databases (Qdrant)
- Serverless relational databases (Neon Postgres)
- Secure, scoped AI responses for educational content

CONSTITUTION RULES (MANDATORY):

1. Grounded Responses Only
- All answers must be grounded in retrieved book content.
- Never fabricate information outside the provided data sources.

2. Source-Scoped Answering
- When user-selected text is provided, responses must rely exclusively on that text.
- If the selected text is insufficient, clearly state the limitation.

3. Architectural Discipline
- Clearly separate ingestion, retrieval, reasoning, and response layers.
- Maintain stateless API design principles.

4. Accuracy Over Fluency
- Prefer precise, correct answers over verbose or creative responses.
- Use clear technical language.

5. Security & Isolation
- Ensure user queries do not leak data across books, chapters, or users.
- Enforce strict context boundaries in retrieval.

6. Educational Quality
- Responses must be clear, structured, and suitable for learners.
- Explain reasoning when helpful, but never expose internal prompts or chain-of-thought.

7. Consistent Terminology
- Use consistent naming for components (embeddings, retriever, agent, tools).
- Do not redefine concepts once established.

8. Professional Tone
- No emojis.
- No casual language.
- Clear, instructional, and production-ready communication.

9. Output Discipline
- Stay strictly within the defined project scope.
- Do not introduce unrelated tools or frameworks.

FINAL INSTRUCTION:
This constitution governs all outputs related to this project.  
Any response that violates these rules is considered invalid.

## Response snapshot

Constitution for the Integrated RAG Chatbot Development project has been successfully created at `.specify/memory/constitution.md`. The new constitution includes all the required principles:

1. Grounded Responses Only
2. Source-Scoped Answering
3. Architectural Discipline
4. Accuracy Over Fluency
5. Security & Isolation
6. Educational Quality

The constitution also includes:
- Technology stack requirements
- Development standards
- Governance information

I have also updated the dependent templates to incorporate the constitution principles:
- `.specify/templates/plan-template.md`: Added a Constitution Check section
- `.specify/templates/spec-template.md`: Added constitution compliance sections for user stories and functional requirements
- `.specify/templates/tasks-template.md`: Added constitution compliance tasks for all user stories

The constitution is version 1.0.0 and has been properly documented with today's date (2025-12-17).

## Outcome

- ✅ Impact: Created comprehensive constitution for RAG chatbot project with 6 core principles
- 🧪 Tests: Updated templates to include constitution compliance checks
- 📁 Files: Modified 4 files to ensure constitution integration
- 🔁 Next prompts: Ready for feature specification and planning
- 🧠 Reflection: Templates now properly enforce constitution principles during feature development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All templates updated consistently with constitution
- Prompt variant (if applicable): Standard constitution creation
- Next experiment (smallest change to try): Begin feature specification using the new templates

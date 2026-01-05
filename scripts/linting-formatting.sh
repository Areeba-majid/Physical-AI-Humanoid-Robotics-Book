# Linting and formatting commands for the AI textbook platform

# Backend (Python)
# Format with black
cd backend && python -m black src/

# Check imports with isort
cd backend && python -m isort src/

# Run mypy for type checking
cd backend && python -m mypy src/

# Run flake8 for linting
cd backend && python -m flake8 src/

# Frontend (JavaScript/TypeScript)
# Format with prettier
cd frontend && npm run format

# Lint with ESLint
cd frontend && npm run lint

# Note: These commands can be run individually or added to your development workflow
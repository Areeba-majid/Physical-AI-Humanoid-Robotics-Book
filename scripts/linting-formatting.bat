@echo off
REM Linting and formatting commands for the AI textbook platform

REM Backend (Python)
echo Formatting backend with black...
cd backend && python -m black src/

echo Checking imports with isort...
cd backend && python -m isort src/

echo Running mypy for type checking...
cd backend && python -m mypy src/

echo Running flake8 for linting...
cd backend && python -m flake8 src/

REM Frontend (JavaScript/TypeScript)
echo Formatting frontend with prettier...
cd ../frontend && npm run format

echo Linting with ESLint...
npm run lint

echo Linting and formatting complete!
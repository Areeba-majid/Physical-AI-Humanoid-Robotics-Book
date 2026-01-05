"""Authentication router for the AI textbook platform."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import hashlib
import secrets

from src.models.user import User, UserCreate
from src.database.repository import BaseRepository
from src.database.connection import get_database

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

# Placeholder for authentication service functionality
# In a real implementation, we would use a proper authentication library like python-jose
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str

# Mock user repository for demonstration
class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, "users")

    async def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return await self.find_one({"email": email})

    async def create_user(self, user_create: UserCreate) -> User:
        """Create a new user."""
        # Hash the password (in a real implementation, use proper password hashing)
        salt = secrets.token_hex(16)
        hashed_password = hashlib.sha256((user_create.password + salt).encode()).hexdigest()

        user = User(
            id=secrets.token_hex(8),  # Generate a simple ID
            email=user_create.email,
            username=user_create.username,
            full_name=user_create.full_name,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        return await self.create(user)

@router.post("/register", response_model=User)
async def register(user_create: UserCreate):
    """Register a new user."""
    user_repo = UserRepository()

    # Check if user already exists
    existing_user = await user_repo.get_by_email(user_create.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )

    # Create the new user
    user = await user_repo.create_user(user_create)
    return user

@router.post("/login", response_model=Token)
async def login(login_request: LoginRequest):
    """Authenticate user and return access token."""
    user_repo = UserRepository()

    # Find user by email
    user = await user_repo.get_by_email(login_request.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # In a real implementation, verify the password hash
    # For this example, we'll just return a mock token
    token = secrets.token_urlsafe(32)

    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=User)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current authenticated user."""
    # In a real implementation, decode and verify the token
    # For this example, we'll just return a mock user
    user = User(
        id="mock_user_id",
        email="user@example.com",
        username="mockuser",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    return user

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    """Logout user."""
    # In a real implementation, you might add the token to a blacklist
    return {"message": "Successfully logged out"}
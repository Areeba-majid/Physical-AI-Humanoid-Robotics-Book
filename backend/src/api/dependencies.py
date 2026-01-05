from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.user import User
from src.utils.auth import get_current_user_from_token


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Get the current user from the JWT token
    """
    token = credentials.credentials
    user_data = get_current_user_from_token(token)
    
    # Fetch user from database
    user = db.query(User).filter(User.username == user_data.get("sub")).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings


# Create the database engine
engine = create_engine(
    settings.NEON_DATABASE_URL,
    pool_pre_ping=True,  # Ensures connections are valid
    pool_recycle=300,    # Recycles connections after 5 minutes
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()


def get_db():
    """
    Dependency function that provides a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""MongoDB connection module for the AI textbook platform."""

import os
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

from src.utils.config import settings

# Global client instance
_client: Optional[AsyncIOMotorClient] = None

async def get_database():
    """Get the database instance."""
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.mongodb_uri)
    return _client[settings.database_name]

async def connect_to_mongo():
    """Initialize the MongoDB connection."""
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.mongodb_uri)
    try:
        # Test the connection
        await _client.admin.command('ping')
        print("Successfully connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

def close_mongo_connection():
    """Close the MongoDB connection."""
    global _client
    if _client:
        _client.close()
        _client = None

def get_sync_client():
    """Get a synchronous MongoDB client for operations that require it."""
    return MongoClient(settings.mongodb_uri)

# Export the client for use in other modules
client = _client
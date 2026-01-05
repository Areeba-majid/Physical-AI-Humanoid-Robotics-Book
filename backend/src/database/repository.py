"""Base repository class for the AI textbook platform.

This module provides a base repository implementation with common
database operations that can be inherited by specific repositories.
"""

from typing import TypeVar, Generic, List, Optional, Dict, Any, Type
from pydantic import BaseModel
from .connection import get_database
from datetime import datetime


# Type variable for Pydantic models
T = TypeVar('T', bound=BaseModel)
TID = TypeVar('TID', str, int)


class BaseRepository(Generic[T]):
    """Base repository with common database operations."""

    def __init__(self, model: Type[T], collection_name: str):
        self.model = model
        self.collection_name = collection_name

    async def get_database(self):
        """Get the database instance."""
        return await get_database()

    async def find_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Find all documents with pagination."""
        db = await self.get_database()
        cursor = db[self.collection_name].find().skip(skip).limit(limit)
        items = []
        async for item in cursor:
            items.append(self.model(**item))
        return items

    async def find_by_id(self, id: str) -> Optional[T]:
        """Find a document by its ID."""
        db = await self.get_database()
        item = await db[self.collection_name].find_one({"_id": id})
        if item:
            return self.model(**item)
        return None

    async def find_many(self, filter_dict: Dict[str, Any]) -> List[T]:
        """Find multiple documents by filter."""
        db = await self.get_database()
        cursor = db[self.collection_name].find(filter_dict)
        items = []
        async for item in cursor:
            items.append(self.model(**item))
        return items

    async def find_one(self, filter_dict: Dict[str, Any]) -> Optional[T]:
        """Find a single document by filter."""
        db = await self.get_database()
        item = await db[self.collection_name].find_one(filter_dict)
        if item:
            return self.model(**item)
        return None

    async def create(self, obj: T) -> T:
        """Create a new document."""
        db = await self.get_database()
        obj_dict = obj.model_dump()
        # Convert datetime fields to MongoDB compatible format
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value
        result = await db[self.collection_name].insert_one(obj_dict)
        obj_dict["_id"] = str(result.inserted_id)
        return self.model(**obj_dict)

    async def update(self, id: str, update_data: Dict[str, Any]) -> Optional[T]:
        """Update an existing document."""
        db = await self.get_database()
        # Add updated_at timestamp
        update_data["updated_at"] = datetime.utcnow()
        result = await db[self.collection_name].update_one(
            {"_id": id},
            {"$set": update_data}
        )
        if result.matched_count:
            updated_item = await db[self.collection_name].find_one({"_id": id})
            return self.model(**updated_item)
        return None

    async def delete(self, id: str) -> bool:
        """Delete a document by ID."""
        db = await self.get_database()
        result = await db[self.collection_name].delete_one({"_id": id})
        return result.deleted_count == 1

    async def count(self, filter_dict: Optional[Dict[str, Any]] = None) -> int:
        """Count documents matching a filter."""
        db = await self.get_database()
        if filter_dict is None:
            filter_dict = {}
        return await db[self.collection_name].count_documents(filter_dict)
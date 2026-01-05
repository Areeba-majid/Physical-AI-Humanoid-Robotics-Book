"""Database utilities for the AI textbook platform.

This module contains functions for initializing the database,
creating indexes, and other database management utilities.
"""

from typing import Dict, Any
from .connection import get_database
from datetime import datetime


async def init_database():
    """Initialize the database with required collections and indexes."""
    db = await get_database()
    
    # Create collections if they don't exist (MongoDB creates them on first use)
    # We'll explicitly create them to ensure they exist
    collections = ["users", "chapters", "quizzes", "progress", "recommendations", "chat_interactions", "translations"]
    
    for collection_name in collections:
        if collection_name not in await db.list_collection_names():
            await db.create_collection(collection_name)
            print(f"Created collection: {collection_name}")
    
    # Create indexes
    await create_indexes(db)
    
    print("Database initialized successfully")


async def create_indexes(db):
    """Create required indexes for performance."""
    # User indexes
    await db["users"].create_index("email", unique=True)
    await db["users"].create_index("username", unique=True)
    await db["users"].create_index("created_at")
    
    # Chapter indexes
    await db["chapters"].create_index("order_index", unique=True)  # For navigation
    await db["chapters"].create_index("status")  # For filtering published vs draft
    await db["chapters"].create_index("created_at")
    await db["chapters"].create_index([("title", "text"), ("content", "text")])  # For search
    
    # Quiz indexes
    await db["quizzes"].create_index("chapter_id")  # For quizzes associated with chapters
    await db["quizzes"].create_index("created_at")
    
    # Progress indexes
    await db["progress"].create_index([("user_id", 1), ("chapter_id", 1)], unique=True)  # For user progress tracking
    await db["progress"].create_index("user_id")  # For user progress queries
    await db["progress"].create_index("chapter_id")  # For chapter progress queries
    await db["progress"].create_index("status")  # For filtering by progress status
    await db["progress"].create_index("created_at")
    
    # Recommendation indexes
    await db["recommendations"].create_index("user_id")  # For user recommendations
    await db["recommendations"].create_index("priority")  # For recommendation priority sorting
    await db["recommendations"].create_index("created_at")
    
    # Chat interaction indexes
    await db["chat_interactions"].create_index("user_id")  # For user chat history
    await db["chat_interactions"].create_index("session_id")  # For session-based queries
    await db["chat_interactions"].create_index("created_at")  # For chronological ordering
    
    # Translation indexes
    await db["translations"].create_index([("original_content_id", 1), ("target_language", 1)], unique=True)
    await db["translations"].create_index("original_content_id")  # For content translations
    await db["translations"].create_index("target_language")  # For language filtering
    await db["translations"].create_index("status")  # For translation workflow
    await db["translations"].create_index("created_at")
    
    print("Indexes created successfully")


async def seed_initial_data():
    """Seed the database with initial data if needed."""
    db = await get_database()
    
    # Check if we already have data
    users_count = await db["users"].count_documents({})
    if users_count > 0:
        print("Database already has data, skipping seeding")
        return
    
    # Add initial chapter if none exist
    chapters_count = await db["chapters"].count_documents({})
    if chapters_count == 0:
        initial_chapter = {
            "title": "Introduction to AI & Robotics",
            "content": "# Introduction to AI & Robotics\n\nThis is the introduction chapter...",
            "content_ur": "# مصنوعی ذہانت اور روبوٹکس کا تعارف\n\nیہ تعارفی باب ہے...",
            "sections": [
                {"title": "What is AI?", "content": "Artificial Intelligence (AI) is intelligence demonstrated by machines..."},
                {"title": "What is Robotics?", "content": "Robotics is an interdisciplinary branch of engineering and science..."}
            ],
            "order_index": 1,
            "word_count": 500,
            "reading_time_estimate": 3,
            "associated_quiz_id": None,
            "status": "published",
            "metadata": {"tags": ["ai", "robotics", "introduction"], "level": "beginner"},
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        result = await db["chapters"].insert_one(initial_chapter)
        print(f"Added initial chapter with ID: {result.inserted_id}")
    
    print("Database seeding completed")


async def reset_database():
    """Reset the database by dropping all collections."""
    db = await get_database()
    
    collections = ["users", "chapters", "quizzes", "progress", "recommendations", "chat_interactions", "translations"]
    
    for collection_name in collections:
        await db[collection_name].drop()
        print(f"Dropped collection: {collection_name}")
    
    print("Database reset completed")
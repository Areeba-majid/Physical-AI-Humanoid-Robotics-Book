"""Embedding utilities for the AI textbook platform.

This module provides functionality for connecting to Qdrant,
creating embeddings, and performing similarity searches.
"""

import os
from typing import List, Optional, Dict, Any
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams
from google.generativeai import embed_content, EmbeddingTaskType
import google.generativeai as genai

from src.utils.config import settings

# Initialize Gemini client with API key
if settings.gemini_api_key:
    genai.configure(api_key=settings.gemini_api_key)

# Qdrant client instance
if settings.qdrant_api_key:
    qdrant_client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
else:
    qdrant_client = QdrantClient(url=settings.qdrant_url)

# Default collection name for textbook embeddings
TEXTBOOK_COLLECTION_NAME = "textbook_content"

# Default embedding dimensions (Gemini embeddings are 768-dimensional)
EMBEDDING_DIM = 768


def initialize_qdrant_collection(collection_name: str = TEXTBOOK_COLLECTION_NAME) -> bool:
    """Initialize a Qdrant collection for storing embeddings."""
    try:
        # Check if collection already exists
        collections = qdrant_client.get_collections()
        collection_names = [collection.name for collection in collections.collections]

        if collection_name not in collection_names:
            # Create a new collection
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE)
            )
            print(f"Created Qdrant collection: {collection_name}")
        else:
            print(f"Qdrant collection {collection_name} already exists")

        return True
    except Exception as e:
        print(f"Error initializing Qdrant collection: {e}")
        return False


def create_embedding(text: str) -> Optional[List[float]]:
    """Create an embedding for the given text using Google's Gemini API."""
    try:
        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")

        # Generate embedding using Gemini
        response = embed_content(
            model="embedding-001",
            content=text,
            task_type=EmbeddingTaskType.RETRIEVAL_DOCUMENT,
        )

        embedding = response['embedding']
        return embedding
    except Exception as e:
        print(f"Error creating embedding: {e}")
        return None


def batch_create_embeddings(texts: List[str]) -> Optional[List[List[float]]]:
    """Create embeddings for a batch of texts."""
    try:
        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")

        embeddings = []
        for text in texts:
            embedding = create_embedding(text)
            if embedding:
                embeddings.append(embedding)
            else:
                # If embedding creation fails for one text, return None for the whole batch
                return None

        return embeddings
    except Exception as e:
        print(f"Error creating batch embeddings: {e}")
        return None


def store_embeddings(
    collection_name: str,
    texts: List[str],
    metadata_list: Optional[List[Dict[str, Any]]] = None,
    ids: Optional[List[str]] = None
) -> bool:
    """Store embeddings in Qdrant collection."""
    try:
        # Create embeddings for the texts
        embeddings = batch_create_embeddings(texts)
        if embeddings is None:
            print("Failed to create embeddings")
            return False

        # If metadata is not provided, create empty metadata for each text
        if metadata_list is None:
            metadata_list = [{}] * len(texts)

        # If IDs are not provided, generate them
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(texts))]

        # Prepare points for Qdrant
        points = []
        for i, (text, embedding, metadata) in enumerate(zip(texts, embeddings, metadata_list)):
            points.append(
                models.PointStruct(
                    id=ids[i],
                    vector=embedding,
                    payload={
                        "text": text,
                        **metadata
                    }
                )
            )

        # Upload points to Qdrant
        qdrant_client.upsert(
            collection_name=collection_name,
            points=points
        )

        print(f"Stored {len(points)} embeddings in collection: {collection_name}")
        return True
    except Exception as e:
        print(f"Error storing embeddings in Qdrant: {e}")
        return False


def search_similar(
    collection_name: str,
    query: str,
    top_k: int = 5,
    filters: Optional[models.Filter] = None
) -> Optional[List[Dict[str, Any]]]:
    """Search for similar content in Qdrant collection."""
    try:
        # Create embedding for the query
        query_embedding = create_embedding(query)
        if query_embedding is None:
            print("Failed to create embedding for query")
            return None

        # Perform search in Qdrant
        search_results = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=top_k,
            query_filter=filters
        )

        # Format results
        results = []
        for hit in search_results:
            results.append({
                "id": hit.id,
                "score": hit.score,
                "text": hit.payload.get("text", ""),
                "metadata": {k: v for k, v in hit.payload.items() if k != "text"}
            })

        return results
    except Exception as e:
        print(f"Error searching similar content: {e}")
        return None


def delete_embeddings(collection_name: str, ids: List[str]) -> bool:
    """Delete embeddings from Qdrant collection by IDs."""
    try:
        qdrant_client.delete(
            collection_name=collection_name,
            points_selector=models.PointIdsList(
                points=ids
            )
        )
        print(f"Deleted {len(ids)} embeddings from collection: {collection_name}")
        return True
    except Exception as e:
        print(f"Error deleting embeddings from Qdrant: {e}")
        return False


def update_embedding(
    collection_name: str,
    id: str,
    text: str,
    metadata: Optional[Dict[str, Any]] = None
) -> bool:
    """Update an existing embedding in Qdrant collection."""
    try:
        # Create new embedding
        new_embedding = create_embedding(text)
        if new_embedding is None:
            print("Failed to create embedding for update")
            return False

        # If metadata is not provided, use empty dict
        if metadata is None:
            metadata = {}

        # Prepare the point with updated data
        point = models.PointStruct(
            id=id,
            vector=new_embedding,
            payload={
                "text": text,
                **metadata
            }
        )

        # Update the point in Qdrant
        qdrant_client.upsert(
            collection_name=collection_name,
            points=[point]
        )

        print(f"Updated embedding with ID: {id}")
        return True
    except Exception as e:
        print(f"Error updating embedding in Qdrant: {e}")
        return False


def get_embedding_count(collection_name: str) -> int:
    """Get the total count of embeddings in a collection."""
    try:
        collection_info = qdrant_client.get_collection(collection_name)
        return collection_info.points_count
    except Exception as e:
        print(f"Error getting embedding count: {e}")
        return 0


def sentence_aware_chunking(text: str, max_chunk_size: int = 1000) -> List[str]:
    """Split text into chunks without breaking sentences."""
    # Split text into sentences
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Group sentences into chunks without exceeding max_chunk_size
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # Check if adding the next sentence would exceed the limit
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += sentence + " "
        else:
            # If the current chunk is not empty, save it
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            # Start a new chunk with the current sentence
            # If a single sentence is longer than max_chunk_size, we'll split it anyway
            if len(sentence) <= max_chunk_size:
                current_chunk = sentence + " "
            else:
                # For very long sentences, split them into smaller parts
                words = sentence.split()
                temp_chunk = ""
                for word in words:
                    if len(temp_chunk) + len(word) <= max_chunk_size:
                        temp_chunk += word + " "
                    else:
                        if temp_chunk.strip():
                            chunks.append(temp_chunk.strip())
                        temp_chunk = word + " "
                current_chunk = temp_chunk

    # Add the last chunk if it's not empty
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


# Initialize the default collection on module import
initialize_qdrant_collection()
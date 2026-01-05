from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Optional, Dict, Any
from uuid import uuid4
import logging
from src.config import settings


class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_CLUSTER_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=True
        )
        self.collection_name = "book_embeddings"
        self.vector_size = 1024  # Cohere base model returns 1024-dim vectors
        self.init_collection()

    def init_collection(self):
        """
        Initialize the Qdrant collection if it doesn't exist
        """
        try:
            self.client.get_collection(collection_name=self.collection_name)
        except:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.COSINE
                )
            )
            # Create payload index for efficient filtering
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="book_id",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="chapter_id",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="section_id",
                field_schema=models.PayloadSchemaType.KEYWORD
            )

    def add_embeddings(self, 
                      book_id: str, 
                      chapter_id: str, 
                      section_id: Optional[str],
                      content: str, 
                      embedding: List[float], 
                      metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a text embedding to the Qdrant collection
        """
        point_id = str(uuid4())
        
        payload = {
            "book_id": book_id,
            "chapter_id": chapter_id,
            "content": content,
            "created_at": str(self.client._rest_client._get_current_timestamp())
        }
        
        if section_id:
            payload["section_id"] = section_id
            
        if metadata:
            payload.update(metadata)
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload
                )
            ]
        )
        
        return point_id

    def search_similar(self, 
                      query_embedding: List[float], 
                      book_id: Optional[str] = None,
                      chapter_id: Optional[str] = None,
                      section_id: Optional[str] = None,
                      limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search for similar content based on embedding
        """
        must_conditions = [
            models.FieldCondition(
                key="book_id",
                match=models.MatchValue(value=book_id)
            )
        ] if book_id else []
        
        if chapter_id:
            must_conditions.append(
                models.FieldCondition(
                    key="chapter_id",
                    match=models.MatchValue(value=chapter_id)
                )
            )
        
        if section_id:
            must_conditions.append(
                models.FieldCondition(
                    key="section_id",
                    match=models.MatchValue(value=section_id)
                )
            )
        
        search_filter = models.Filter(must=must_conditions) if must_conditions else None
        
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            query_filter=search_filter,
            limit=limit
        )
        
        return [
            {
                "id": result.id,
                "content": result.payload["content"],
                "book_id": result.payload["book_id"],
                "chapter_id": result.payload["chapter_id"],
                "section_id": result.payload.get("section_id"),
                "score": result.score
            }
            for result in results
        ]

    def delete_by_book_id(self, book_id: str):
        """
        Delete all embeddings associated with a book
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="book_id",
                            match=models.MatchValue(value=book_id)
                        )
                    ]
                )
            )
        )

    def delete_by_ids(self, ids: List[str]):
        """
        Delete embeddings by their IDs
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.PointIdsList(
                points=ids
            )
        )


# Global instance
qdrant_service = QdrantService()
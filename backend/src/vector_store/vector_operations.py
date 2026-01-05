import cohere
from typing import List
from src.config import settings


class EmbeddingService:
    def __init__(self):
        self.client = cohere.Client(settings.COHERE_API_KEY)
    
    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts using Cohere
        """
        response = self.client.embed(
            texts=texts,
            model="embed-english-v3.0",  # Using Cohere's English v3 embedding model
            input_type="search_document"  # Optimize for search documents
        )
        return response.embeddings

    def generate_query_embedding(self, query: str) -> List[float]:
        """
        Generate embedding for a query text using Cohere
        """
        response = self.client.embed(
            texts=[query],
            model="embed-english-v3.0",
            input_type="search_query"  # Optimize for search queries
        )
        return response.embeddings[0]


# Global instance
embedding_service = EmbeddingService()
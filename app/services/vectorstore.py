import chromadb
from chromadb.config import Settings
from typing import List

class VectorStore:
    def __init__(self, collection_name: str):
        self.client = chromadb.Client(
            Settings(anonymized_telemetry=False)
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, docs: List[str], embeddings: List[List[float]]):
        ids = [f"doc_{i}" for i in range(len(docs))]
        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query_embedding, k: int = 3):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results

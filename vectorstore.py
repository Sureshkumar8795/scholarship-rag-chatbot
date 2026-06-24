import chromadb
from typing import List

# Create/load local database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="scholarship_chunks"
)

def store_chunks(chunks: List[str], embeddings: List[List[float]]):

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB")


def search_chunks(query_embedding, top_k=3):

    results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
    )
    

    return results
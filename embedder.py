from sentence_transformers import SentenceTransformer
from typing import List

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings.tolist()
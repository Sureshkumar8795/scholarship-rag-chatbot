from vectorstore import search_chunks
from embedder import embed_chunks

def retrieve_context(query, top_k=3):

    query_embedding = embed_chunks([query])[0]

    results = search_chunks(
        query_embedding,
        top_k=top_k
    )

    return results["documents"][0]
# test_retriever.py

from retriever import retrieve_context

query = "What scholarships are available for SC students?"

results = retrieve_context(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results, 1):
    print(f"\nChunk {i}")
    print("-" * 50)
    print(chunk)
from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_chunks

pdf_path = "scholar_ship_details.pdf"

def run():

    # Step 1: Read PDF
    pages = read_pdf(pdf_path)

    print(f"Extracted {len(pages)} pages from the PDF")

    if pages:
        print("\n--- First Page Preview ---")
        print(pages[0][:500])
    else:
        print("No content found.")
        return

    # Step 2: Create Chunks
    chunks = chunk_pages(
        pages,
        chunk_size=900,
        chunk_overlap=150
    )

    print(f"\nTotal chunks created: {len(chunks)}")

    if chunks:
        print("\n--- First Chunk Preview ---")
        print(chunks[0][:500])
    else:
        print("No chunks were created.")
        return

    # Step 3: Create Embeddings
    embeddings = embed_chunks(chunks)

    print(f"\nTotal embeddings created: {len(embeddings)}")

    if embeddings:
        print(f"Embedding dimension: {len(embeddings[0])}")
    else:
        print("No embeddings were created.")
        return

    # Step 4: Store in ChromaDB
    store_chunks(chunks, embeddings)

    print("\n✅ Successfully stored chunks in ChromaDB")

    # Test Output
    print("\n--- Storage Summary ---")
    print(f"Pages      : {len(pages)}")
    print(f"Chunks     : {len(chunks)}")
    print(f"Embeddings : {len(embeddings)}")

if __name__ == "__main__":
    run()
from typing import List

def chunk_pages(
    pages: List[str],
    chunk_size: int = 500,
    chunk_overlap: int = 150
) -> List[str]:

    chunks = []

    full_text = "\n".join(pages)

    start = 0

    while start < len(full_text):
        end = min(start + chunk_size, len(full_text))

        chunk = full_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(full_text):
            break

        start = end - chunk_overlap

    return chunks
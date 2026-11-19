class DocumentChunker:
    """
    Contract & Specification document chunker with hierarchical metadata injection
    designed to maintain regulatory context across chunk boundaries.
    """
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 150):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_technical_text(self, document_text: str, document_name: str, standard_code: str):
        words = document_text.split()
        chunks = []
        start = 0
        chunk_idx = 1
        
        while start < len(words):
            end = min(start + self.chunk_size, len(words))
            chunk_content = " ".join(words[start:end])
            
            chunks.append({
                'chunk_id': f"{standard_code}_c{chunk_idx}",
                'document': document_name,
                'standard_code': standard_code,
                'content': chunk_content,
                'word_count': end - start
            })
            if end == len(words):
                break
            start += (self.chunk_size - self.chunk_overlap)
            chunk_idx += 1
            
        return chunks

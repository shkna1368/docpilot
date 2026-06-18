CREATE INDEX IF NOT EXISTS idx_rag_embedding
    ON rag_documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

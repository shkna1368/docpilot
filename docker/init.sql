CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS rag_documents (
    embedding_id UUID PRIMARY KEY,
    embedding vector(384),
    text TEXT,
    metadata JSONB
);

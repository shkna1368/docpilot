"""
End-to-end integration test:
1. Starts a PostgreSQL+pgvector container
2. Loads the generated SQL files
3. Runs a similarity search query
4. Validates results from multiple frameworks
"""
import subprocess
import time
import sys
import os
import psycopg2
import numpy as np
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))
from src.embedder import embed_texts

CONTAINER_NAME = "framework-docs-test-pg"
PG_PORT = 5433  # avoid conflict with local pg
PG_USER = "docs"
PG_PASS = "docs"
PG_DB = "frameworkdocs"
OUTPUT_DIR = Path(__file__).parent / "output"


def start_postgres():
    """Start a pgvector-enabled PostgreSQL container."""
    print("Starting PostgreSQL+pgvector container...")
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], capture_output=True)
    subprocess.run([
        "docker", "run", "-d", "--name", CONTAINER_NAME,
        "-e", f"POSTGRES_USER={PG_USER}",
        "-e", f"POSTGRES_PASSWORD={PG_PASS}",
        "-e", f"POSTGRES_DB={PG_DB}",
        "-p", f"{PG_PORT}:5432",
        "pgvector/pgvector:pg17",
    ], check=True)

    # Wait for pg to be ready
    for _ in range(30):
        try:
            conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
            conn.close()
            print("  PostgreSQL ready!")
            return
        except Exception:
            time.sleep(1)
    raise RuntimeError("PostgreSQL did not start in time")


def load_schema_and_data():
    """Load schema and SQL data files."""
    conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
    conn.autocommit = True
    cur = conn.cursor()

    # Create extension and table
    print("Creating schema...")
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rag_documents (
            embedding_id UUID PRIMARY KEY,
            embedding vector(384),
            text TEXT,
            metadata JSONB
        );
    """)

    # Load SQL files
    sql_files = sorted(OUTPUT_DIR.glob("*.sql"))
    total_rows = 0
    for sql_file in sql_files:
        if sql_file.stat().st_size == 0:
            continue
        print(f"  Loading {sql_file.name}...")
        content = sql_file.read_text()
        statements = [s.strip() for s in content.split("\n") if s.strip().startswith("INSERT")]
        for stmt in statements:
            try:
                cur.execute(stmt)
                total_rows += 1
            except Exception as e:
                print(f"    ERROR: {e}")
                break

    print(f"  Loaded {total_rows} document chunks")

    # Create index
    print("  Creating ivfflat index...")
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_rag_embedding
        ON rag_documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 10);
    """)

    cur.close()
    conn.close()
    return total_rows


def search(query: str, framework: str = None, top_k: int = 5):
    """Run a similarity search."""
    embedding = embed_texts([query])[0]
    emb_str = "[" + ",".join(str(v) for v in embedding) + "]"

    conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
    cur = conn.cursor()

    if framework:
        cur.execute("""
            SELECT text, metadata, 1 - (embedding <=> %s::vector) as score
            FROM rag_documents
            WHERE metadata->>'source' = %s
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (emb_str, framework, emb_str, top_k))
    else:
        cur.execute("""
            SELECT text, metadata, 1 - (embedding <=> %s::vector) as score
            FROM rag_documents
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (emb_str, emb_str, top_k))

    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def cleanup():
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], capture_output=True)


def main():
    try:
        start_postgres()
        total = load_schema_and_data()
        assert total > 0, "No data loaded!"

        print("\n=== SEARCH TESTS ===\n")

        # Test 1: General query
        print("Test 1: 'routing middleware' (no filter)")
        results = search("routing middleware")
        assert len(results) > 0, "No results!"
        for text, meta, score in results[:3]:
            print(f"  [{meta['source']}] score={score:.3f}: {text[:80]}...")
        print("  ✅ PASSED\n")

        # Test 2: Framework-filtered query
        print("Test 2: 'dependency injection' (filter: fastapi)")
        results = search("dependency injection", framework="fastapi")
        assert len(results) > 0, "No results!"
        for text, meta, score in results[:3]:
            assert meta["source"] == "fastapi", f"Wrong source: {meta['source']}"
            print(f"  [{meta['source']}] score={score:.3f}: {text[:80]}...")
        print("  ✅ PASSED\n")

        # Test 3: Spring-specific query
        print("Test 3: 'security authentication oauth' (filter: spring-security)")
        results = search("security authentication oauth", framework="spring-security")
        assert len(results) > 0, "No results!"
        for text, meta, score in results[:3]:
            assert meta["source"] == "spring-security"
            print(f"  [{meta['source']}] score={score:.3f}: {text[:80]}...")
        print("  ✅ PASSED\n")

        # Test 4: Go Fiber query
        print("Test 4: 'route parameters handler' (filter: go-fiber)")
        results = search("route parameters handler", framework="go-fiber")
        assert len(results) > 0, "No results!"
        for text, meta, score in results[:3]:
            assert meta["source"] == "go-fiber"
            print(f"  [{meta['source']}] score={score:.3f}: {text[:80]}...")
        print("  ✅ PASSED\n")

        # Test 5: Cross-framework relevance
        print("Test 5: 'how to create REST endpoint' (no filter - should return multiple frameworks)")
        results = search("how to create REST endpoint", top_k=10)
        sources = set(meta["source"] for _, meta, _ in results)
        print(f"  Frameworks in results: {sources}")
        assert len(sources) >= 2, f"Expected multiple frameworks, got: {sources}"
        print("  ✅ PASSED\n")

        print("=" * 40)
        print("ALL TESTS PASSED ✅")
        print(f"Total chunks in DB: {total}")
        print(f"Frameworks tested: go-fiber, fastapi, spring-security, cross-framework")

    finally:
        cleanup()


if __name__ == "__main__":
    main()

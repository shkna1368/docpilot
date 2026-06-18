"""
Performance benchmark: measures embed + pgvector query latency.
Uses the test PG container (framework-docs-test-pg on port 5433).
"""
import subprocess, time, sys, os
from pathlib import Path

import psycopg2

sys.path.insert(0, str(Path(__file__).parent))
from src.embedder import embed_texts

CONTAINER_NAME = "framework-docs-test-pg"
PG_PORT = 5433
PG_USER = "docs"
PG_PASS = "docs"
PG_DB = "frameworkdocs"
OUTPUT_DIR = Path(__file__).parent / "output"

QUERIES = [
    "fiber routing middleware",
    "spring boot dependency injection",
    "fastapi path parameters",
    "django orm query",
    "kafka consumer configuration",
]


def ensure_pg():
    """Start PG container if not running, load data if empty."""
    try:
        conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM rag_documents")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        if count > 0:
            print(f"PG ready with {count} chunks")
            return
    except Exception:
        pass

    # Start container
    print("Starting PG container...")
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], capture_output=True)
    subprocess.run([
        "docker", "run", "-d", "--name", CONTAINER_NAME,
        "-e", f"POSTGRES_USER={PG_USER}", "-e", f"POSTGRES_PASSWORD={PG_PASS}",
        "-e", f"POSTGRES_DB={PG_DB}", "-p", f"{PG_PORT}:5432",
        "pgvector/pgvector:pg17",
    ], check=True)

    for _ in range(30):
        try:
            conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
            conn.close()
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError("PG did not start")

    # Load schema + data
    conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cur.execute("""CREATE TABLE IF NOT EXISTS rag_documents (
        embedding_id UUID PRIMARY KEY, embedding vector(384), text TEXT, metadata JSONB);""")

    total = 0
    for sql_file in sorted(OUTPUT_DIR.glob("*.sql")):
        if sql_file.stat().st_size == 0:
            continue
        for line in sql_file.read_text().splitlines():
            if line.strip().startswith("INSERT"):
                try:
                    cur.execute(line)
                    total += 1
                except Exception:
                    break

    cur.execute("""CREATE INDEX IF NOT EXISTS idx_rag_embedding
        ON rag_documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 10);""")
    cur.close()
    conn.close()
    print(f"Loaded {total} chunks")


def bench_query(conn, query: str) -> float:
    """Time a single embed + pgvector search. Returns seconds."""
    t0 = time.perf_counter()
    embedding = embed_texts([query])[0]
    emb_str = "[" + ",".join(str(v) for v in embedding) + "]"
    cur = conn.cursor()
    cur.execute("""
        SELECT text, metadata, 1 - (embedding <=> %s::vector) as score
        FROM rag_documents ORDER BY embedding <=> %s::vector LIMIT 5
    """, (emb_str, emb_str))
    cur.fetchall()
    cur.close()
    return time.perf_counter() - t0


def main():
    ensure_pg()
    conn = psycopg2.connect(host="localhost", port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB)

    # Warmup
    print("\nWarmup...")
    bench_query(conn, "warmup query")

    print("\n=== BENCHMARK (embed + pgvector search) ===\n")
    latencies = []
    for q in QUERIES:
        t = bench_query(conn, q)
        latencies.append(t)
        print(f"  {t*1000:7.1f} ms  | {q}")

    print(f"\n{'─'*45}")
    print(f"  Min: {min(latencies)*1000:.1f} ms")
    print(f"  Max: {max(latencies)*1000:.1f} ms")
    print(f"  Avg: {sum(latencies)/len(latencies)*1000:.1f} ms")
    print(f"{'─'*45}")
    conn.close()


if __name__ == "__main__":
    main()

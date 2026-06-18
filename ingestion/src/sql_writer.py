import json
import uuid


def generate_sql(chunks: list[tuple[str, list[float], dict]], output_path: str):
    with open(output_path, "w") as f:
        for text, embedding, metadata in chunks:
            eid = uuid.uuid4()
            emb = "[" + ",".join(f"{v:.8f}" for v in embedding) + "]"
            # Escape for PostgreSQL E'' string: backslash-escape single quotes and newlines
            txt = text.replace("\\", "\\\\").replace("'", "''").replace("\n", "\\n").replace("\r", "\\r")
            meta = json.dumps(metadata).replace("\\", "\\\\").replace("'", "''")
            f.write(f"INSERT INTO rag_documents VALUES ('{eid}','{emb}',E'{txt}','{meta}');\n")

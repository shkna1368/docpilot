import json
import uuid


def generate_sql(chunks: list[tuple[str, list[float], dict]], output_path: str):
    with open(output_path, "w") as f:
        for text, embedding, metadata in chunks:
            eid = uuid.uuid4()
            emb = "[" + ",".join(f"{v:.8f}" for v in embedding) + "]"
            # Text: use E'' with backslash escaping for newlines/quotes
            txt = text.replace("\\", "\\\\").replace("'", "''").replace("\n", "\\n").replace("\r", "\\r")
            # Metadata: plain string literal, only escape single quotes (JSON handles its own escaping)
            meta = json.dumps(metadata).replace("'", "''")
            f.write(f"INSERT INTO rag_documents VALUES ('{eid}','{emb}',E'{txt}','{meta}');\n")

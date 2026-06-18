import tempfile
from src.sql_writer import generate_sql


def _gen(text="hello", metadata=None):
    if metadata is None:
        metadata = {"source": "test", "title": "t"}
    embedding = [0.1, 0.2, 0.3]
    path = tempfile.mktemp(suffix=".sql")
    generate_sql([(text, embedding, metadata)], path)
    return open(path).read()


def test_valid_insert_statement():
    sql = _gen()
    assert sql.startswith("INSERT INTO rag_documents VALUES (")
    assert sql.strip().endswith(");")


def test_single_quotes_escaped():
    sql = _gen("it's a test")
    assert "it''s a test" in sql


def test_newlines_escaped():
    sql = _gen("line1\nline2")
    assert "\\n" in sql
    assert "\n" not in sql.split("E'")[1].split("'")[0].replace("\\n", "")


def test_backslashes_escaped():
    sql = _gen("path\\to\\file")
    assert "path\\\\to\\\\file" in sql


def test_metadata_json_escaped():
    sql = _gen(metadata={"title": "it's", "key": "val"})
    # metadata section should have escaped quotes
    assert "it''s" in sql

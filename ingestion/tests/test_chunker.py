from src.scraper import DocPage
from src.chunker import chunk_page


def _page(text, title="Test"):
    return DocPage(url="http://x", title=title, section_title="", text=text,
                   source="test", version="1.0", language="python", topics="", categories="")


def test_header_splitting():
    text = "## Section A\n" + "Content A " * 10 + "\n\n## Section B\n" + "Content B " * 10
    chunks = chunk_page(_page(text))
    texts = [c[0] for c in chunks]
    assert any("Section A" in t for t in texts)
    assert any("Section B" in t for t in texts)


def test_small_sections_stay_intact():
    text = "## Title\n" + "x" * 200
    chunks = chunk_page(_page(text))
    assert len(chunks) == 1
    assert "x" * 200 in chunks[0][0]


def test_large_sections_get_subdivided():
    text = "## Big Section\n" + ("word " * 300)
    chunks = chunk_page(_page(text))
    assert len(chunks) > 1


def test_section_title_prefixed_to_subchunks():
    text = "## My Title\n" + ("word " * 300)
    chunks = chunk_page(_page(text))
    for chunk_text, _ in chunks:
        assert chunk_text.startswith("My Title")


def test_chunks_below_50_chars_filtered():
    text = "## Tiny\nHi\n\n## Real Section\n" + "content " * 20
    chunks = chunk_page(_page(text))
    for chunk_text, _ in chunks:
        assert len(chunk_text.strip()) >= 50


def test_no_headers_fallback():
    text = "Just plain text without any headers. " * 5
    chunks = chunk_page(_page(text))
    assert len(chunks) >= 1
    assert "plain text" in chunks[0][0]

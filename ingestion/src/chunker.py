import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .scraper import DocPage

MAX_CHUNK = 1000
MIN_CHUNK = 50

_sub_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " "]
)

# Matches markdown (#), asciidoc (= or ==), and rst (underlines) headers
_HEADER_RE = re.compile(r"^(#{1,4}\s+.+|={1,5}\s+.+)$", re.MULTILINE)


def _split_by_headers(text: str) -> list[tuple[str, str]]:
    """Split text into (section_title, body) pairs by headers."""
    sections = []
    lines = text.split("\n")
    current_title = ""
    current_body = []

    for line in lines:
        if _HEADER_RE.match(line.strip()):
            # Save previous section
            if current_body:
                body = "\n".join(current_body).strip()
                if body:
                    sections.append((current_title, body))
            current_title = line.strip().lstrip("#=").strip()
            current_body = []
        else:
            current_body.append(line)

    # Last section
    if current_body:
        body = "\n".join(current_body).strip()
        if body:
            sections.append((current_title, body))

    return sections


def chunk_page(page: DocPage) -> list[tuple[str, dict]]:
    sections = _split_by_headers(page.text)

    # If no headers found, treat whole text as one section
    if not sections:
        sections = [("", page.text)]

    chunks = []
    for section_title, body in sections:
        if len(body) <= MAX_CHUNK:
            # Keep as single chunk
            chunk_text = f"{section_title}\n\n{body}" if section_title else body
            chunks.append(chunk_text)
        else:
            # Split large sections, prefix sub-chunks with section title
            sub_chunks = _sub_splitter.split_text(body)
            for sub in sub_chunks:
                chunk_text = f"{section_title}\n\n{sub}" if section_title else sub
                chunks.append(chunk_text)

    metadata = {
        "source": page.source, "version": page.version,
        "language": page.language, "title": page.title,
        "section_title": page.section_title, "url": page.url,
        "topics": page.topics, "categories": page.categories,
    }

    return [(chunk, metadata) for chunk in chunks if len(chunk.strip()) >= MIN_CHUNK]

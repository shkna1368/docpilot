# Adding a New Framework

## Step 1: Create a Scraper

Create a new file in `ingestion/src/scrapers/`:

```python
from .github_base import GitHubDocsScraper


class MyFrameworkScraper(GitHubDocsScraper):
    repo = "org/repo"              # GitHub repo
    branch = "main"                # Branch to fetch from
    source = "my-framework"        # Unique ID
    version = "1.0"                # Framework version
    language = "python"            # Programming language
    topics_prefix = "myframework"  # Comma-separated topic tags
    categories = "web,python"      # Comma-separated categories
    paths = [                      # Doc files to scrape
        "docs/guide.md",
        "docs/api.md",
        "docs/configuration.md",
    ]
```

### Tips for Choosing Paths

- Look for markdown (`.md`) or AsciiDoc (`.adoc`) files in the repo's `docs/` directory
- Prioritize guides, tutorials, and API references over changelogs
- Each path should have at least 100 characters of content
- Start with 5-15 core documentation files

## Step 2: Register in CLI

Edit `ingestion/src/cli.py`:

```python
# Add import
from .scrapers.my_framework import MyFrameworkScraper

# Add to SCRAPERS dict
SCRAPERS["my-framework"] = MyFrameworkScraper()
```

## Step 3: Run Ingestion

```bash
cd ingestion
python -m src.cli scrape --framework my-framework
```

This will:
1. Fetch docs from GitHub
2. Split into chunks by headers
3. Generate embeddings (BGE Small EN v1.5)
4. Write SQL to `ingestion/output/my-framework-1.0.sql`

## Step 4: Rebuild Docker Image

```bash
docker build -t framework-docs-mcp:latest .
```

The SQL file is automatically copied into the PostgreSQL init directory during the Docker build.

## Step 5: Update README

Add your framework to the appropriate table in `README.md`.

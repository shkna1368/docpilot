import httpx
from ..scraper import BaseScraper, DocPage


class GitHubDocsScraper(BaseScraper):
    """Base scraper that fetches markdown files directly from GitHub repos."""

    repo: str  # e.g. "gofiber/docs"
    branch: str = "main"
    paths: list[str] = []  # e.g. ["docs/guide/routing.md"]
    source: str = ""
    version: str = ""
    language: str = ""
    topics_prefix: str = ""
    categories: str = ""

    def scrape(self) -> list[DocPage]:
        pages = []
        client = httpx.Client(timeout=30, follow_redirects=True)
        base = f"https://raw.githubusercontent.com/{self.repo}/{self.branch}"

        for path in self.paths:
            url = f"{base}/{path}"
            try:
                resp = client.get(url)
                if resp.status_code != 200:
                    continue
                text = resp.text.strip()
                if len(text) < 100:
                    continue

                # Extract title from first heading
                title = path.split("/")[-1].replace(".md", "").replace("-", " ").title()
                for line in text.split("\n"):
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break

                section = path.split("/")[-1].replace(".md", "")
                github_url = f"https://github.com/{self.repo}/blob/{self.branch}/{path}"

                pages.append(DocPage(
                    url=github_url, title=title, section_title=section,
                    text=text, source=self.source, version=self.version,
                    language=self.language,
                    topics=self.topics_prefix + "," + section.replace("-", ","),
                    categories=self.categories,
                ))
            except Exception:
                continue
        client.close()
        return pages

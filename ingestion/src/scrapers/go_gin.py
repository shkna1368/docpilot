from .github_base import GitHubDocsScraper


class GinScraper(GitHubDocsScraper):
    repo = "gin-gonic/gin"
    branch = "master"
    source = "go-gin"
    version = "1.12"
    language = "go"
    topics_prefix = "gin,http"
    categories = "web,go,rest"
    paths = [
        "docs/doc.md",
    ]

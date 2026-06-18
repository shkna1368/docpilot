from .github_base import GitHubDocsScraper


class ElasticsearchScraper(GitHubDocsScraper):
    repo = "elastic/elasticsearch"
    branch = "main"
    source = "elasticsearch"
    version = "8"
    language = "json"
    topics_prefix = "elasticsearch,search"
    categories = "database,search,analytics"
    paths = [
        "docs/README.md",
    ]

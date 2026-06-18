from .github_base import GitHubDocsScraper


class AxumScraper(GitHubDocsScraper):
    repo = "tokio-rs/axum"
    branch = "main"
    source = "axum"
    version = "0.8"
    language = "rust"
    topics_prefix = "axum,tokio"
    categories = "web,rust,rest,async"
    paths = [
        "axum/README.md",
        "axum-core/README.md",
        "axum-extra/README.md",
    ]

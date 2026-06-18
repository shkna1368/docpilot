from .github_base import GitHubDocsScraper


class EchoScraper(GitHubDocsScraper):
    repo = "labstack/echo"
    branch = "master"
    source = "go-echo"
    version = "5.1"
    language = "go"
    topics_prefix = "echo,http"
    categories = "web,go,rest"
    paths = [
        "README.md",
    ]

from .github_base import GitHubDocsScraper


class ActixWebScraper(GitHubDocsScraper):
    repo = "actix/actix-web"
    branch = "master"
    source = "actix-web"
    version = "4.13"
    language = "rust"
    topics_prefix = "actix,http,async"
    categories = "web,rust,rest,async"
    paths = [
        "README.md",
        "actix-web/README.md",
    ]

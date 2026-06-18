from .github_base import GitHubDocsScraper


class LaravelScraper(GitHubDocsScraper):
    repo = "laravel/docs"
    branch = "12.x"
    source = "laravel"
    version = "12"
    language = "php"
    topics_prefix = "laravel,php"
    categories = "web,php,fullstack,orm"
    paths = [
        "routing.md",
        "controllers.md",
        "eloquent.md",
        "middleware.md",
        "authentication.md",
        "migrations.md",
    ]

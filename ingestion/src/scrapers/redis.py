from .github_base import GitHubDocsScraper


class RedisScraper(GitHubDocsScraper):
    repo = "redis/docs"
    branch = "main"
    source = "redis"
    version = "7.4"
    language = "nosql"
    topics_prefix = "redis"
    categories = "database,nosql,cache"
    paths = [
        "README.md",
    ]

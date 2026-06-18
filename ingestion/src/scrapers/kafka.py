from .github_base import GitHubDocsScraper


class KafkaScraper(GitHubDocsScraper):
    repo = "apache/kafka"
    branch = "trunk"
    source = "kafka"
    version = "4.0"
    language = "java"
    topics_prefix = "kafka"
    categories = "messaging,streaming,java"
    paths = [
        "README.md",
    ]

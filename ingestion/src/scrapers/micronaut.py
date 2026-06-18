from .github_base import GitHubDocsScraper


class MicronautScraper(GitHubDocsScraper):
    repo = "micronaut-projects/micronaut-core"
    branch = "4.7.x"
    source = "micronaut"
    version = "4.7"
    language = "java"
    topics_prefix = "micronaut,java"
    categories = "web,java,rest,cloud-native"
    paths = [
        "README.md",
        "src/main/docs/guide/introduction.adoc",
    ]

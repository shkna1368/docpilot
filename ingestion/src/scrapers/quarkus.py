from .github_base import GitHubDocsScraper


class QuarkusScraper(GitHubDocsScraper):
    repo = "quarkusio/quarkusio.github.io"
    branch = "main"
    source = "quarkus"
    version = "3.36"
    language = "java"
    topics_prefix = "quarkus"
    categories = "web,java,rest,enterprise"
    paths = [
        "_guides/getting-started.adoc",
        "_guides/rest.adoc",
        "_guides/hibernate-orm.adoc",
        "_guides/hibernate-orm-panache.adoc",
        "_guides/security-overview.adoc",
        "_guides/cdi-reference.adoc",
        "_guides/config-reference.adoc",
        "_guides/getting-started-testing.adoc",
        "_guides/getting-started-reactive.adoc",
    ]

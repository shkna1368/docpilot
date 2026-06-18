from .github_base import GitHubDocsScraper


class HibernateScraper(GitHubDocsScraper):
    repo = "hibernate/hibernate-orm"
    branch = "main"
    source = "hibernate"
    version = "7.0"
    language = "java"
    topics_prefix = "hibernate,orm,jpa"
    categories = "java,database,orm,persistence"
    paths = [
        "documentation/src/main/asciidoc/introduction/Configuration.adoc",
        "documentation/src/main/asciidoc/introduction/Entities.adoc",
        "documentation/src/main/asciidoc/introduction/Mapping.adoc",
        "documentation/src/main/asciidoc/introduction/Querying.adoc",
        "documentation/src/main/asciidoc/introduction/Sessions.adoc",
        "documentation/src/main/asciidoc/introduction/Tuning.adoc",
        "documentation/src/main/asciidoc/introduction/Interacting.adoc",
        "documentation/src/main/asciidoc/introduction/Fetching.adoc",
        "documentation/src/main/asciidoc/introduction/Generator.adoc",
        "documentation/src/main/asciidoc/introduction/Caching.adoc",
    ]

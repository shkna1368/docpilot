from .github_base import GitHubDocsScraper


class SpringDataScraper(GitHubDocsScraper):
    repo = "spring-projects/spring-data-jpa"
    branch = "main"
    source = "spring-data"
    version = "2024"
    language = "java"
    topics_prefix = "spring,data,jpa"
    categories = "java,database,jpa,repository"
    paths = [
        "src/main/antora/modules/ROOT/pages/jpa/query-methods.adoc",
        "src/main/antora/modules/ROOT/pages/jpa/repositories.adoc",
        "src/main/antora/modules/ROOT/pages/jpa/entity-persistence.adoc",
    ]

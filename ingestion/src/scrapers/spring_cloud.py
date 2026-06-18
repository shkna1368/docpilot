from .github_base import GitHubDocsScraper


class SpringCloudScraper(GitHubDocsScraper):
    repo = "spring-cloud/spring-cloud-gateway"
    branch = "4.1.x"
    source = "spring-cloud"
    version = "2024"
    language = "java"
    topics_prefix = "spring,cloud,gateway"
    categories = "java,microservices,cloud,distributed"
    paths = [
        "docs/modules/ROOT/pages/spring-cloud-gateway/how-it-works.adoc",
        "docs/modules/ROOT/pages/spring-cloud-gateway/configuring-route-predicate-factories-and-filter-factories.adoc",
        "docs/modules/ROOT/pages/spring-cloud-gateway/global-filters.adoc",
        "docs/modules/ROOT/pages/spring-cloud-gateway/gatewayfilter-factories.adoc",
    ]

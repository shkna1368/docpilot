from .github_base import GitHubDocsScraper


class SpringFrameworkScraper(GitHubDocsScraper):
    repo = "spring-projects/spring-framework"
    branch = "main"
    source = "spring-framework"
    version = "7"
    language = "java"
    topics_prefix = "spring,framework"
    categories = "java,enterprise,ioc,web"
    paths = [
        "framework-docs/modules/ROOT/pages/core/beans/definition.adoc",
        "framework-docs/modules/ROOT/pages/core/beans/dependencies.adoc",
        "framework-docs/modules/ROOT/pages/core/beans/factory-scopes.adoc",
        "framework-docs/modules/ROOT/pages/core/beans/annotation-config.adoc",
        "framework-docs/modules/ROOT/pages/core/aop.adoc",
        "framework-docs/modules/ROOT/pages/core/expressions.adoc",
        "framework-docs/modules/ROOT/pages/web/webmvc.adoc",
        "framework-docs/modules/ROOT/pages/web/webflux.adoc",
        "framework-docs/modules/ROOT/pages/data-access/transaction.adoc",
        "framework-docs/modules/ROOT/pages/data-access/jdbc.adoc",
        "framework-docs/modules/ROOT/pages/testing.adoc",
        "framework-docs/modules/ROOT/pages/integration/rest-clients.adoc",
    ]

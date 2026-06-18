from .github_base import GitHubDocsScraper


class SpringBootScraper(GitHubDocsScraper):
    repo = "spring-projects/spring-boot"
    branch = "3.4.x"
    source = "spring-boot"
    version = "4.0"
    language = "java"
    topics_prefix = "spring,boot"
    categories = "web,java,rest,enterprise"
    paths = [
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/web/servlet.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/web/reactive.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/data/sql.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/messaging/kafka.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/io/caching.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/io/validation.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/io/rest-client.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/actuator/endpoints.adoc",
        "spring-boot-project/spring-boot-docs/src/docs/antora/modules/reference/pages/testing/spring-boot-applications.adoc",
    ]

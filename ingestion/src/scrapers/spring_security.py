from .github_base import GitHubDocsScraper


class SpringSecurityScraper(GitHubDocsScraper):
    repo = "spring-projects/spring-security"
    branch = "main"
    source = "spring-security"
    version = "7"
    language = "java"
    topics_prefix = "spring,security"
    categories = "java,security,auth,oauth2"
    paths = [
        "docs/modules/ROOT/pages/servlet/authentication/architecture.adoc",
        "docs/modules/ROOT/pages/servlet/authorization/authorize-http-requests.adoc",
        "docs/modules/ROOT/pages/servlet/authorization/method-security.adoc",
        "docs/modules/ROOT/pages/servlet/exploits/csrf.adoc",
        "docs/modules/ROOT/pages/servlet/configuration/java.adoc",
        "docs/modules/ROOT/pages/reactive/authentication.adoc",
        "docs/modules/ROOT/pages/reactive/authorization.adoc",
    ]

from .github_base import GitHubDocsScraper


class DjangoScraper(GitHubDocsScraper):
    repo = "django/django"
    branch = "main"
    source = "django"
    version = "6.0"
    language = "python"
    topics_prefix = "django"
    categories = "web,python,rest,orm"
    paths = [
        "docs/intro/tutorial01.txt",
        "docs/topics/http/urls.txt",
        "docs/topics/http/views.txt",
        "docs/topics/http/middleware.txt",
        "docs/topics/db/models.txt",
        "docs/topics/db/queries.txt",
        "docs/topics/forms/index.txt",
        "docs/topics/auth/default.txt",
        "docs/topics/testing/overview.txt",
    ]

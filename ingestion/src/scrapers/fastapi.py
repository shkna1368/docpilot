from .github_base import GitHubDocsScraper


class FastAPIScraper(GitHubDocsScraper):
    repo = "fastapi/fastapi"
    branch = "master"
    source = "fastapi"
    version = "0.136"
    language = "python"
    topics_prefix = "fastapi,async"
    categories = "web,python,rest,async"
    paths = [
        "docs/en/docs/tutorial/first-steps.md",
        "docs/en/docs/tutorial/path-params.md",
        "docs/en/docs/tutorial/query-params.md",
        "docs/en/docs/tutorial/body.md",
        "docs/en/docs/tutorial/dependencies/index.md",
        "docs/en/docs/tutorial/security/index.md",
        "docs/en/docs/tutorial/middleware.md",
        "docs/en/docs/tutorial/sql-databases.md",
        "docs/en/docs/tutorial/testing.md",
        "docs/en/docs/tutorial/bigger-applications.md",
        "docs/en/docs/tutorial/background-tasks.md",
        "docs/en/docs/tutorial/response-model.md",
    ]

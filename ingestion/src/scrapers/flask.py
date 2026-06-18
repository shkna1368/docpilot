from .github_base import GitHubDocsScraper


class FlaskScraper(GitHubDocsScraper):
    repo = "pallets/flask"
    branch = "main"
    source = "flask"
    version = "3.1.3"
    language = "python"
    topics_prefix = "flask"
    categories = "web,python,rest"
    paths = [
        "docs/quickstart.rst",
        "docs/blueprints.rst",
        "docs/tutorial/factory.rst",
        "docs/tutorial/database.rst",
        "docs/tutorial/views.rst",
        "docs/testing.rst",
        "docs/errorhandling.rst",
        "docs/config.rst",
    ]

from .github_base import GitHubDocsScraper


class RocketScraper(GitHubDocsScraper):
    repo = "rwf2/Rocket"
    branch = "v0.5-rc"
    source = "rocket"
    version = "0.6"
    language = "rust"
    topics_prefix = "rocket,http"
    categories = "web,rust,rest"
    paths = [
        "site/guide/2-getting-started.md",
        "site/guide/3-overview.md",
        "site/guide/4-requests.md",
        "site/guide/5-responses.md",
        "site/guide/6-state.md",
        "site/guide/7-fairings.md",
        "site/guide/8-testing.md",
        "site/guide/9-configuration.md",
    ]

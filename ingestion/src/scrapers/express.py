from .github_base import GitHubDocsScraper


class ExpressScraper(GitHubDocsScraper):
    repo = "expressjs/express"
    branch = "master"
    source = "express"
    version = "4.22"
    language = "javascript"
    topics_prefix = "express,node"
    categories = "web,javascript,rest"
    paths = [
        "Readme.md",
    ]

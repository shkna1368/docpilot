from .github_base import GitHubDocsScraper


class HelmScraper(GitHubDocsScraper):
    repo = "helm/helm"
    branch = "main"
    source = "helm"
    version = "3.16"
    language = "yaml"
    topics_prefix = "helm,kubernetes,charts"
    categories = "devops,kubernetes,packaging"
    paths = [
        "README.md",
    ]

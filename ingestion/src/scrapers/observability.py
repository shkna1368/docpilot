from .github_base import GitHubDocsScraper


class PrometheusScraper(GitHubDocsScraper):
    repo = "prometheus/prometheus"
    branch = "main"
    source = "prometheus"
    version = "2.54"
    language = "yaml"
    topics_prefix = "prometheus,monitoring,metrics"
    categories = "devops,monitoring,observability"
    paths = [
        "README.md",
    ]


class GrafanaScraper(GitHubDocsScraper):
    repo = "grafana/grafana"
    branch = "main"
    source = "grafana"
    version = "11"
    language = "json"
    topics_prefix = "grafana,dashboards,visualization"
    categories = "devops,monitoring,observability"
    paths = [
        "README.md",
    ]


class VaultScraper(GitHubDocsScraper):
    repo = "hashicorp/vault"
    branch = "main"
    source = "vault"
    version = "1.17"
    language = "hcl"
    topics_prefix = "vault,secrets,security"
    categories = "devops,security,secrets"
    paths = [
        "README.md",
    ]

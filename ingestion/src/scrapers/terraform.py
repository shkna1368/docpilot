from .github_base import GitHubDocsScraper


class TerraformScraper(GitHubDocsScraper):
    repo = "hashicorp/terraform"
    branch = "main"
    source = "terraform"
    version = "1.9"
    language = "hcl"
    topics_prefix = "terraform,iac"
    categories = "devops,infrastructure,cloud"
    paths = [
        "docs/README.md",
        "docs/architecture.md",
        "docs/resource-instance-change-lifecycle.md",
        "docs/destroying.md",
        "CHANGELOG.md",
    ]

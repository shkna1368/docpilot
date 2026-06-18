from .github_base import GitHubDocsScraper


class PyTorchScraper(GitHubDocsScraper):
    repo = "pytorch/pytorch"
    branch = "main"
    source = "pytorch"
    version = "2.4"
    language = "python"
    topics_prefix = "pytorch,deeplearning,tensor"
    categories = "ai,deeplearning,ml"
    paths = [
        "README.md",
    ]

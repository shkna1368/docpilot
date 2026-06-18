from .github_base import GitHubDocsScraper


class TensorFlowScraper(GitHubDocsScraper):
    repo = "tensorflow/tensorflow"
    branch = "master"
    source = "tensorflow"
    version = "2.17"
    language = "python"
    topics_prefix = "tensorflow,deeplearning,ml"
    categories = "ai,deeplearning,ml"
    paths = [
        "README.md",
    ]

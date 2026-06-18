from .github_base import GitHubDocsScraper


class ScikitLearnScraper(GitHubDocsScraper):
    repo = "scikit-learn/scikit-learn"
    branch = "main"
    source = "scikit-learn"
    version = "1.5"
    language = "python"
    topics_prefix = "sklearn,ml,classification"
    categories = "ai,ml,classification,regression"
    paths = ["README.rst"]


class MLflowScraper(GitHubDocsScraper):
    repo = "mlflow/mlflow"
    branch = "master"
    source = "mlflow"
    version = "2.16"
    language = "python"
    topics_prefix = "mlflow,mlops,tracking"
    categories = "ai,mlops,experiment-tracking"
    paths = ["README.md"]

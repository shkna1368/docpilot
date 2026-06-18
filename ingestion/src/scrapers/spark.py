from .github_base import GitHubDocsScraper


class SparkScraper(GitHubDocsScraper):
    repo = "apache/spark"
    branch = "master"
    source = "spark"
    version = "3.5"
    language = "python"
    topics_prefix = "spark,bigdata,sql"
    categories = "bigdata,analytics,ml,streaming"
    paths = [
        "docs/quick-start.md",
        "docs/sql-programming-guide.md",
        "docs/structured-streaming-programming-guide.md",
        "docs/rdd-programming-guide.md",
        "docs/ml-guide.md",
        "docs/cluster-overview.md",
    ]

from .github_base import GitHubDocsScraper


class MongoDBScraper(GitHubDocsScraper):
    repo = "mongodb/docs"
    branch = "master"
    source = "mongodb"
    version = "7"
    language = "nosql"
    topics_prefix = "mongodb,nosql"
    categories = "database,nosql,document"
    paths = [
        "source/crud.txt",
        "source/core/aggregation-pipeline.txt",
        "source/indexes.txt",
        "source/core/schema-validation.txt",
    ]

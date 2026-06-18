from .github_base import GitHubDocsScraper


class OracleGoScraper(GitHubDocsScraper):
    repo = "godror/godror"
    branch = "main"
    source = "oracle"
    version = "23"
    language = "go"
    topics_prefix = "oracle,go,sql"
    categories = "database,sql,oracle"
    paths = ["README.md"]


class OracleNodeScraper(GitHubDocsScraper):
    repo = "oracle/node-oracledb"
    branch = "main"
    source = "oracle"
    version = "23"
    language = "javascript"
    topics_prefix = "oracle,node,sql"
    categories = "database,sql,oracle"
    paths = ["README.md"]


class OraclePythonScraper(GitHubDocsScraper):
    repo = "oracle/python-oracledb"
    branch = "main"
    source = "oracle"
    version = "23"
    language = "python"
    topics_prefix = "oracle,python,sql"
    categories = "database,sql,oracle"
    paths = ["README.md"]

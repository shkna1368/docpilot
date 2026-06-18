from .github_base import GitHubDocsScraper


class MySQLScraper(GitHubDocsScraper):
    repo = "mysql/mysql-server"
    branch = "trunk"
    source = "mysql"
    version = "9.0"
    language = "sql"
    topics_prefix = "mysql"
    categories = "database,sql,relational"
    paths = [
        "README",
    ]

from .github_base import GitHubDocsScraper


class MySQLServerScraper(GitHubDocsScraper):
    repo = "mysql/mysql-server"
    branch = "trunk"
    source = "mysql"
    version = "9.0"
    language = "sql"
    topics_prefix = "mysql"
    categories = "database,sql,relational"
    paths = [
        "README",
        "CONTRIBUTING.md",
    ]


class MySQLShellScraper(GitHubDocsScraper):
    repo = "mysql/mysql-shell"
    branch = "master"
    source = "mysql"
    version = "9.0"
    language = "sql"
    topics_prefix = "mysql/shell"
    categories = "database,sql,relational,shell,cli"
    paths = [
        "README.md",
        "INSTALL.md",
    ]


class MySQLOperatorScraper(GitHubDocsScraper):
    repo = "mysql/mysql-operator"
    branch = "trunk"
    source = "mysql"
    version = "9.0"
    language = "sql"
    topics_prefix = "mysql/operator"
    categories = "database,sql,relational,kubernetes,operator"
    paths = [
        "README.md",
    ]


class MySQLConnectorJScraper(GitHubDocsScraper):
    repo = "mysql/mysql-connector-j"
    branch = "release/9.x"
    source = "mysql"
    version = "9.0"
    language = "java"
    topics_prefix = "mysql/connector-j"
    categories = "database,sql,relational,java,jdbc"
    paths = [
        "README.md",
    ]


class MySQLConnectorPythonScraper(GitHubDocsScraper):
    repo = "mysql/mysql-connector-python"
    branch = "trunk"
    source = "mysql"
    version = "9.0"
    language = "python"
    topics_prefix = "mysql/connector-python"
    categories = "database,sql,relational,python"
    paths = [
        "README.rst",
    ]

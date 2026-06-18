from .github_base import GitHubDocsScraper


class PostgreSQLScraper(GitHubDocsScraper):
    repo = "postgres/postgres"
    branch = "master"
    source = "postgresql"
    version = "17"
    language = "sql"
    topics_prefix = "postgresql,postgres"
    categories = "database,sql,relational"
    paths = [
        "doc/src/sgml/queries.sgml",
        "doc/src/sgml/ddl.sgml",
        "doc/src/sgml/dml.sgml",
        "doc/src/sgml/indices.sgml",
        "doc/src/sgml/mvcc.sgml",
        "doc/src/sgml/perform.sgml",
        "doc/src/sgml/config.sgml",
    ]

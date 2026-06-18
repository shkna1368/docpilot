from .github_base import GitHubDocsScraper


class SqlxScraper(GitHubDocsScraper):
    repo = "launchbadge/sqlx"
    branch = "main"
    source = "sqlx"
    version = "0.8"
    language = "rust"
    topics_prefix = "sqlx,rust,sql,async"
    categories = "database,sql,rust,async"
    paths = ["README.md"]


class TonicScraper(GitHubDocsScraper):
    repo = "hyperium/tonic"
    branch = "master"
    source = "grpc"
    version = "1.60"
    language = "rust"
    topics_prefix = "tonic,grpc,rust,protobuf"
    categories = "rpc,rust,microservices"
    paths = ["README.md"]


class SeaOrmScraper(GitHubDocsScraper):
    repo = "SeaQL/sea-orm"
    branch = "master"
    source = "sea-orm"
    version = "1.0"
    language = "rust"
    topics_prefix = "seaorm,rust,orm,async"
    categories = "database,orm,rust,async"
    paths = ["README.md"]

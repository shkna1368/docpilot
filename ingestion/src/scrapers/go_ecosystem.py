from .github_base import GitHubDocsScraper


class GoRedisScraper(GitHubDocsScraper):
    repo = "redis/go-redis"
    branch = "master"
    source = "redis"
    version = "7"
    language = "go"
    topics_prefix = "redis,go,cache"
    categories = "database,cache,go"
    paths = ["README.md"]


class PgxScraper(GitHubDocsScraper):
    repo = "jackc/pgx"
    branch = "master"
    source = "postgresql"
    version = "17"
    language = "go"
    topics_prefix = "postgresql,pgx,go,sql"
    categories = "database,sql,go"
    paths = ["README.md"]


class GrpcGoScraper(GitHubDocsScraper):
    repo = "grpc/grpc-go"
    branch = "master"
    source = "grpc"
    version = "1.60"
    language = "go"
    topics_prefix = "grpc,go,protobuf"
    categories = "rpc,go,microservices"
    paths = ["README.md"]


class SqlcScraper(GitHubDocsScraper):
    repo = "sqlc-dev/sqlc"
    branch = "main"
    source = "postgresql"
    version = "17"
    language = "go"
    topics_prefix = "sqlc,go,sql,codegen"
    categories = "database,sql,go,codegen"
    paths = ["README.md"]

from .github_base import GitHubDocsScraper


class RedisScraper(GitHubDocsScraper):
    repo = "redis/redis"
    branch = "unstable"
    source = "redis"
    version = "7.4"
    language = "nosql"
    topics_prefix = "redis"
    categories = "database,nosql,cache"
    paths = [
        "README.md",
    ]


class RedisDocScraper(GitHubDocsScraper):
    repo = "redis/redis-doc"
    branch = "master"
    source = "redis"
    version = "7.4"
    language = "nosql"
    topics_prefix = "redis"
    categories = "database,nosql,cache"
    paths = [
        "docs/connect/cli.md",
        "docs/management/persistence.md",
        "docs/management/replication.md",
        "docs/management/config.md",
        "docs/management/sentinel.md",
        "docs/management/admin.md",
        "docs/management/troubleshooting.md",
        "docs/management/debugging.md",
        "docs/management/optimization/memory-optimization.md",
        "docs/management/optimization/latency.md",
        "docs/reference/cluster-spec.md",
        "docs/data-types/strings.md",
        "docs/data-types/lists.md",
        "docs/data-types/hashes.md",
        "docs/data-types/sets.md",
        "docs/data-types/sorted-sets.md",
        "docs/data-types/streams.md",
        "docs/interact/pubsub.md",
        "docs/interact/transactions.md",
        "docs/interact/programmability/eval-intro.md",
        "docs/interact/programmability/lua-api.md",
    ]

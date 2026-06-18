from .github_base import GitHubDocsScraper


class GrpcScraper(GitHubDocsScraper):
    repo = "grpc/grpc.io"
    branch = "main"
    source = "grpc"
    version = "1.65"
    language = "proto"
    topics_prefix = "grpc,rpc"
    categories = "rpc,networking,proto"
    paths = [
        "content/en/docs/what-is-grpc/introduction.md",
        "content/en/docs/what-is-grpc/core-concepts.md",
        "content/en/docs/guides/auth.md",
        "content/en/docs/guides/error.md",
        "content/en/docs/guides/deadlines.md",
        "content/en/docs/guides/keepalive.md",
        "content/en/docs/guides/flow-control.md",
        "content/en/docs/guides/retry.md",
        "content/en/docs/languages/python/basics.md",
    ]

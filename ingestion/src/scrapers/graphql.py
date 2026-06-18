from .github_base import GitHubDocsScraper


class GraphQLScraper(GitHubDocsScraper):
    repo = "graphql/graphql.github.io"
    branch = "source"
    source = "graphql"
    version = "1.0"
    language = "graphql"
    topics_prefix = "graphql"
    categories = "api,query,graphql"
    paths = [
        "src/pages/learn/index.mdx",
        "src/pages/learn/queries.mdx",
        "src/pages/learn/schema.mdx",
        "src/pages/learn/thinking-in-graphs.mdx",
        "src/pages/learn/serving-over-http.mdx",
        "src/pages/learn/best-practices.mdx",
        "src/pages/learn/pagination.mdx",
    ]

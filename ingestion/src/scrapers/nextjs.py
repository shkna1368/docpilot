from .github_base import GitHubDocsScraper


class NextJSScraper(GitHubDocsScraper):
    repo = "vercel/next.js"
    branch = "canary"
    source = "nextjs"
    version = "15"
    language = "typescript"
    topics_prefix = "nextjs,react,ssr"
    categories = "web,typescript,fullstack,ssr"
    paths = [
        "docs/01-app/01-getting-started/01-installation.mdx",
        "docs/01-app/01-getting-started/02-project-structure.mdx",
        "docs/01-app/01-getting-started/03-layouts-and-pages.mdx",
        "docs/01-app/01-getting-started/06-fetching-data.mdx",
    ]

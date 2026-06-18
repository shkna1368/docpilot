from .github_base import GitHubDocsScraper


class NuxtScraper(GitHubDocsScraper):
    repo = "nuxt/nuxt"
    branch = "main"
    source = "nuxtjs"
    version = "3"
    language = "typescript"
    topics_prefix = "nuxt,vue,ssr"
    categories = "web,typescript,fullstack,ssr"
    paths = [
        "README.md",
    ]

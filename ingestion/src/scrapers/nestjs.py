from .github_base import GitHubDocsScraper


class NestJSScraper(GitHubDocsScraper):
    repo = "nestjs/docs.nestjs.com"
    branch = "master"
    source = "nestjs"
    version = "11"
    language = "typescript"
    topics_prefix = "nestjs,typescript"
    categories = "web,typescript,rest,enterprise"
    paths = [
        "content/controllers.md",
        "content/providers.md",
        "content/modules.md",
        "content/middleware.md",
        "content/guards.md",
        "content/interceptors.md",
        "content/pipes.md",
        "content/exception-filters.md",
    ]

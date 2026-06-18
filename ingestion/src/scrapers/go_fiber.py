from .github_base import GitHubDocsScraper


class GoFiberScraper(GitHubDocsScraper):
    repo = "gofiber/fiber"
    branch = "main"
    source = "go-fiber"
    version = "3.3"
    language = "go"
    topics_prefix = "fiber,http"
    categories = "web,go,rest"
    paths = [
        "docs/guide/routing.md",
        "docs/guide/grouping.md",
        "docs/guide/templates.md",
        "docs/guide/error-handling.md",
        "docs/guide/validation.md",
        "docs/api/ctx.md",
        "docs/api/app.md",
        "docs/api/fiber.md",
    ]

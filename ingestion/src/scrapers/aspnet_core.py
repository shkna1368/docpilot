from .github_base import GitHubDocsScraper


class AspNetCoreScraper(GitHubDocsScraper):
    repo = "dotnet/AspNetCore.Docs"
    branch = "main"
    source = "aspnet-core"
    version = "10"
    language = "csharp"
    topics_prefix = "aspnet,dotnet"
    categories = "web,csharp,rest,enterprise"
    paths = [
        "aspnetcore/fundamentals/routing.md",
        "aspnetcore/fundamentals/middleware/index.md",
        "aspnetcore/fundamentals/dependency-injection.md",
        "aspnetcore/fundamentals/error-handling.md",
        "aspnetcore/mvc/controllers/actions.md",
        "aspnetcore/web-api/index.md",
        "aspnetcore/security/authentication/index.md",
    ]

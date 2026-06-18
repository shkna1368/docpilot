from .github_base import GitHubDocsScraper


class CrewAIScraper(GitHubDocsScraper):
    repo = "crewAIInc/crewAI"
    branch = "main"
    source = "crewai"
    version = "0.80"
    language = "python"
    topics_prefix = "crewai,agents,multi-agent"
    categories = "ai,agents,orchestration"
    paths = [
        "README.md",
    ]

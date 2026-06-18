from .github_base import GitHubDocsScraper


class OpenAIScraper(GitHubDocsScraper):
    repo = "openai/openai-python"
    branch = "main"
    source = "openai"
    version = "1.0"
    language = "python"
    topics_prefix = "openai,gpt,llm"
    categories = "ai,llm,api"
    paths = [
        "README.md",
    ]


class AnthropicScraper(GitHubDocsScraper):
    repo = "anthropics/anthropic-sdk-python"
    branch = "main"
    source = "anthropic"
    version = "1.0"
    language = "python"
    topics_prefix = "anthropic,claude,llm"
    categories = "ai,llm,api"
    paths = [
        "README.md",
    ]

from .github_base import GitHubDocsScraper


class LangChainScraper(GitHubDocsScraper):
    repo = "langchain-ai/langchain"
    branch = "master"
    source = "langchain"
    version = "0.3"
    language = "python"
    topics_prefix = "langchain,llm,rag"
    categories = "ai,llm,agents,rag"
    paths = [
        "README.md",
        "libs/langchain/README.md",
        "libs/core/README.md",
    ]

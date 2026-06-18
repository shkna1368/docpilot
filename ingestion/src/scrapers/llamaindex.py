from .github_base import GitHubDocsScraper


class LlamaIndexScraper(GitHubDocsScraper):
    repo = "run-llama/llama_index"
    branch = "main"
    source = "llamaindex"
    version = "0.11"
    language = "python"
    topics_prefix = "llamaindex,rag,llm"
    categories = "ai,rag,llm,embeddings"
    paths = [
        "README.md",
    ]

from .github_base import GitHubDocsScraper


class SpringAIScraper(GitHubDocsScraper):
    repo = "spring-projects/spring-ai"
    branch = "main"
    source = "spring-ai"
    version = "1.0"
    language = "java"
    topics_prefix = "spring,ai,llm"
    categories = "ai,java,llm,embeddings"
    paths = [
        "README.md",
        "spring-ai-docs/src/main/antora/modules/ROOT/pages/index.adoc",
        "spring-ai-docs/src/main/antora/modules/ROOT/pages/api/chat/openai-chat.adoc",
        "spring-ai-docs/src/main/antora/modules/ROOT/pages/api/embeddings.adoc",
        "spring-ai-docs/src/main/antora/modules/ROOT/pages/api/vectordbs.adoc",
    ]

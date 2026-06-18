from .github_base import GitHubDocsScraper


class TransformersScraper(GitHubDocsScraper):
    repo = "huggingface/transformers"
    branch = "main"
    source = "transformers"
    version = "4.44"
    language = "python"
    topics_prefix = "transformers,huggingface,nlp"
    categories = "ai,nlp,deeplearning,llm"
    paths = [
        "docs/source/en/index.md",
        "docs/source/en/quicktour.md",
        "docs/source/en/pipeline_tutorial.md",
        "docs/source/en/training.md",
        "docs/source/en/llm_tutorial.md",
    ]

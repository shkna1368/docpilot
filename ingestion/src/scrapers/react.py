from .github_base import GitHubDocsScraper


class ReactScraper(GitHubDocsScraper):
    repo = "reactjs/react.dev"
    branch = "main"
    source = "react"
    version = "19"
    language = "typescript"
    topics_prefix = "react,hooks"
    categories = "web,typescript,frontend,spa"
    paths = [
        "src/content/learn/index.md",
        "src/content/learn/thinking-in-react.md",
        "src/content/learn/managing-state.md",
        "src/content/learn/passing-props-to-a-component.md",
        "src/content/learn/responding-to-events.md",
        "src/content/learn/synchronizing-with-effects.md",
        "src/content/learn/referencing-values-with-refs.md",
        "src/content/reference/react/hooks.md",
    ]

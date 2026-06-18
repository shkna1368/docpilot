from .github_base import GitHubDocsScraper


class AndroidScraper(GitHubDocsScraper):
    repo = "android/nowinandroid"
    branch = "main"
    source = "android"
    version = "15"
    language = "kotlin"
    topics_prefix = "android,kotlin,compose"
    categories = "mobile,android,ui"
    paths = [
        "README.md",
    ]


class AndroidComposeScraper(GitHubDocsScraper):
    repo = "android/compose-samples"
    branch = "main"
    source = "android"
    version = "15"
    language = "kotlin"
    topics_prefix = "android,compose,jetpack"
    categories = "mobile,android,ui"
    paths = [
        "README.md",
    ]


class AndroidArchScraper(GitHubDocsScraper):
    repo = "android/architecture-samples"
    branch = "main"
    source = "android"
    version = "15"
    language = "kotlin"
    topics_prefix = "android,architecture,mvvm"
    categories = "mobile,android,architecture"
    paths = [
        "README.md",
    ]

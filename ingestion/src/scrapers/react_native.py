from .github_base import GitHubDocsScraper


class ReactNativeScraper(GitHubDocsScraper):
    repo = "facebook/react-native-website"
    branch = "main"
    source = "react-native"
    version = "0.74"
    language = "typescript"
    topics_prefix = "react-native,mobile"
    categories = "mobile,cross-platform,javascript"
    paths = [
        "docs/getting-started.md",
        "docs/components-and-apis.md",
        "docs/navigation.md",
        "docs/network.md",
        "docs/style.md",
        "docs/flexbox.md",
        "docs/performance.md",
    ]

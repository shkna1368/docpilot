from .github_base import GitHubDocsScraper


class FlutterScraper(GitHubDocsScraper):
    repo = "flutter/flutter"
    branch = "master"
    source = "flutter"
    version = "3.24"
    language = "dart"
    topics_prefix = "flutter,dart,mobile"
    categories = "mobile,cross-platform,ui"
    paths = [
        "docs/README.md",
    ]


class FlutterSamplesScraper(GitHubDocsScraper):
    repo = "flutter/samples"
    branch = "main"
    source = "flutter"
    version = "3.24"
    language = "dart"
    topics_prefix = "flutter,dart,mobile"
    categories = "mobile,cross-platform,ui"
    paths = [
        "README.md",
    ]

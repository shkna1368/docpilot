from .github_base import GitHubDocsScraper


class SwiftScraper(GitHubDocsScraper):
    repo = "swiftlang/swift-book"
    branch = "main"
    source = "ios-swift"
    version = "6.0"
    language = "swift"
    topics_prefix = "swift,ios,apple"
    categories = "mobile,ios,apple"
    paths = [
        "TSPL.docc/GuidedTour/GuidedTour.md",
        "TSPL.docc/LanguageGuide/TheBasics.md",
        "TSPL.docc/LanguageGuide/ControlFlow.md",
        "TSPL.docc/LanguageGuide/Functions.md",
        "TSPL.docc/LanguageGuide/ClassesAndStructures.md",
        "TSPL.docc/LanguageGuide/Protocols.md",
        "TSPL.docc/LanguageGuide/Concurrency.md",
    ]

from .github_base import GitHubDocsScraper


class GitScraper(GitHubDocsScraper):
    repo = "progit/progit2"
    branch = "main"
    source = "git"
    version = "2"
    language = "bash"
    topics_prefix = "git,vcs,branching"
    categories = "devops,vcs,scm"
    paths = [
        "book/01-introduction/sections/about-version-control.asc",
        "book/02-git-basics/sections/recording-changes.asc",
        "book/02-git-basics/sections/viewing-history.asc",
        "book/02-git-basics/sections/remotes.asc",
        "book/03-git-branching/sections/nutshell.asc",
        "book/03-git-branching/sections/basic-branching-and-merging.asc",
        "book/03-git-branching/sections/rebasing.asc",
        "book/07-git-tools/sections/reset.asc",
    ]

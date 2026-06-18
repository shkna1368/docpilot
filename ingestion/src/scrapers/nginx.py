from .github_base import GitHubDocsScraper


class NginxScraper(GitHubDocsScraper):
    repo = "nginx/unit"
    branch = "master"
    source = "nginx"
    version = "1.27"
    language = "conf"
    topics_prefix = "nginx,proxy,http"
    categories = "devops,webserver,proxy"
    paths = [
        "README.md",
    ]

from .github_base import GitHubDocsScraper


class NATSScraper(GitHubDocsScraper):
    repo = "nats-io/nats-server"
    branch = "main"
    source = "nats"
    version = "2.10"
    language = "go"
    topics_prefix = "nats,messaging,pubsub"
    categories = "messaging,streaming,cloud-native"
    paths = ["README.md"]

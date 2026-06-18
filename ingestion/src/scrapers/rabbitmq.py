from .github_base import GitHubDocsScraper


class RabbitMQScraper(GitHubDocsScraper):
    repo = "rabbitmq/rabbitmq-website"
    branch = "main"
    source = "rabbitmq"
    version = "3.13"
    language = "amqp"
    topics_prefix = "rabbitmq,messaging"
    categories = "messaging,queue,amqp"
    paths = [
        "docs/queues.md",
        "docs/consumers.md",
        "docs/exchanges.md",
        "docs/reliability.md",
        "docs/clustering.md",
    ]

from .github_base import GitHubDocsScraper


class KafkaPythonScraper(GitHubDocsScraper):
    repo = "dpkp/kafka-python"
    branch = "master"
    source = "kafka"
    version = "3.9"
    language = "python"
    topics_prefix = "kafka,consumer,producer,python"
    categories = "messaging,streaming,python"
    paths = ["README.rst"]


class KafkaGoScraper(GitHubDocsScraper):
    repo = "confluentinc/confluent-kafka-go"
    branch = "master"
    source = "kafka"
    version = "3.9"
    language = "go"
    topics_prefix = "kafka,consumer,producer,go"
    categories = "messaging,streaming,go"
    paths = ["README.md"]


class KafkaRustScraper(GitHubDocsScraper):
    repo = "fede1024/rust-rdkafka"
    branch = "master"
    source = "kafka"
    version = "3.9"
    language = "rust"
    topics_prefix = "kafka,rdkafka,consumer,producer"
    categories = "messaging,streaming,rust"
    paths = ["README.md"]

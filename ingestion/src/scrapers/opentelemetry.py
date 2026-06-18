from .github_base import GitHubDocsScraper


class OpenTelemetryScraper(GitHubDocsScraper):
    repo = "open-telemetry/opentelemetry.io"
    branch = "main"
    source = "opentelemetry"
    version = "1.0"
    language = "yaml"
    topics_prefix = "otel,observability,tracing"
    categories = "devops,observability,monitoring"
    paths = [
        "content/en/docs/concepts/signals/traces.md",
        "content/en/docs/concepts/signals/metrics.md",
        "content/en/docs/concepts/signals/logs.md",
    ]

from .github_base import GitHubDocsScraper


class RailsScraper(GitHubDocsScraper):
    repo = "rails/rails"
    branch = "main"
    source = "rails"
    version = "8"
    language = "ruby"
    topics_prefix = "rails,ruby"
    categories = "web,ruby,fullstack,orm"
    paths = [
        "guides/source/getting_started.md",
        "guides/source/routing.md",
        "guides/source/active_record_basics.md",
        "guides/source/action_controller_overview.md",
        "guides/source/active_record_migrations.md",
    ]

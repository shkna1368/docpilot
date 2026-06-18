from .github_base import GitHubDocsScraper


class AngularScraper(GitHubDocsScraper):
    repo = "angular/angular"
    branch = "main"
    source = "angular"
    version = "19"
    language = "typescript"
    topics_prefix = "angular,typescript"
    categories = "web,typescript,frontend,spa"
    paths = [
        "adev/src/content/introduction/what-is-angular.md",
        "adev/src/content/guide/components/lifecycle.md",
        "adev/src/content/guide/components/inputs.md",
        "adev/src/content/guide/components/outputs.md",
        "adev/src/content/guide/routing/common-router-tasks.md",
        "adev/src/content/guide/routing/router-reference.md",
        "adev/src/content/guide/forms/reactive-forms.md",
        "adev/src/content/guide/forms/overview.md",
        "adev/src/content/guide/http/making-requests.md",
        "adev/src/content/guide/http/setup.md",
        "adev/src/content/guide/testing/components-basics.md",
    ]

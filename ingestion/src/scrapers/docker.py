from .github_base import GitHubDocsScraper


class DockerScraper(GitHubDocsScraper):
    repo = "docker/docs"
    branch = "main"
    source = "docker"
    version = "27"
    language = "dockerfile"
    topics_prefix = "docker,container"
    categories = "devops,containers,deployment"
    paths = [
        "content/get-started/docker-concepts/the-basics/what-is-a-container.md",
        "content/get-started/docker-concepts/the-basics/what-is-an-image.md",
        "content/get-started/docker-concepts/building-images/writing-a-dockerfile.md",
        "content/get-started/docker-concepts/building-images/understanding-image-layers.md",
        "content/get-started/docker-concepts/building-images/build-tag-and-publish-an-image.md",
        "content/get-started/docker-concepts/running-containers/publishing-ports.md",
        "content/get-started/docker-concepts/running-containers/multi-container-applications.md",
    ]


class DockerComposeScraper(GitHubDocsScraper):
    repo = "compose-spec/compose-spec"
    branch = "main"
    source = "docker"
    version = "27"
    language = "yaml"
    topics_prefix = "docker,compose,services"
    categories = "devops,containers,orchestration"
    paths = [
        "spec.md",
        "01-status.md",
        "02-model.md",
        "03-compose-file.md",
        "04-version-and-name.md",
        "05-services.md",
        "06-networks.md",
        "07-volumes.md",
        "08-configs.md",
        "09-secrets.md",
        "10-fragments.md",
        "11-extension.md",
        "12-interpolation.md",
        "13-merge.md",
    ]

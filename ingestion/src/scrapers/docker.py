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

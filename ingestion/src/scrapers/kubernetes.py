from .github_base import GitHubDocsScraper


class KubernetesScraper(GitHubDocsScraper):
    repo = "kubernetes/website"
    branch = "main"
    source = "kubernetes"
    version = "1.31"
    language = "yaml"
    topics_prefix = "kubernetes,k8s"
    categories = "devops,orchestration,cloud"
    paths = [
        "content/en/docs/concepts/workloads/pods/_index.md",
        "content/en/docs/concepts/workloads/controllers/deployment.md",
        "content/en/docs/concepts/workloads/controllers/statefulset.md",
        "content/en/docs/concepts/workloads/controllers/daemonset.md",
        "content/en/docs/concepts/workloads/controllers/job.md",
        "content/en/docs/concepts/services-networking/service.md",
        "content/en/docs/concepts/configuration/configmap.md",
        "content/en/docs/concepts/configuration/secret.md",
        "content/en/docs/concepts/storage/persistent-volumes.md",
    ]

from .github_base import GitHubDocsScraper


class JenkinsScraper(GitHubDocsScraper):
    repo = "jenkins-infra/jenkins.io"
    branch = "master"
    source = "jenkins"
    version = "2.4"
    language = "groovy"
    topics_prefix = "jenkins,ci,pipeline"
    categories = "devops,ci,automation"
    paths = [
        "content/doc/book/pipeline/syntax.adoc",
        "content/doc/book/pipeline/jenkinsfile.adoc",
        "content/doc/book/pipeline/getting-started.adoc",
        "content/doc/book/pipeline/shared-libraries.adoc",
        "content/doc/book/pipeline/docker.adoc",
        "content/doc/book/managing/plugins.adoc",
        "content/doc/book/security/access-control.adoc",
    ]

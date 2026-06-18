from .github_base import GitHubDocsScraper


class TraefikScraper(GitHubDocsScraper):
    repo = "traefik/traefik"
    branch = "master"
    source = "traefik"
    version = "3"
    language = "yaml"
    topics_prefix = "traefik,proxy,ingress"
    categories = "devops,proxy,cloud-native"
    paths = ["README.md"]


class EnvoyScraper(GitHubDocsScraper):
    repo = "envoyproxy/envoy"
    branch = "main"
    source = "envoy"
    version = "1.31"
    language = "yaml"
    topics_prefix = "envoy,proxy,mesh"
    categories = "devops,proxy,service-mesh"
    paths = ["README.md"]


class IstioScraper(GitHubDocsScraper):
    repo = "istio/istio"
    branch = "master"
    source = "istio"
    version = "1.23"
    language = "yaml"
    topics_prefix = "istio,mesh,kubernetes"
    categories = "devops,service-mesh,kubernetes"
    paths = ["README.md"]


class ArgoCDScraper(GitHubDocsScraper):
    repo = "argoproj/argo-cd"
    branch = "master"
    source = "argocd"
    version = "2.12"
    language = "yaml"
    topics_prefix = "argocd,gitops,kubernetes"
    categories = "devops,gitops,kubernetes"
    paths = ["README.md"]


class PulumiScraper(GitHubDocsScraper):
    repo = "pulumi/pulumi"
    branch = "master"
    source = "pulumi"
    version = "3"
    language = "typescript"
    topics_prefix = "pulumi,iac,cloud"
    categories = "devops,infrastructure,cloud"
    paths = ["README.md"]


class KeycloakScraper(GitHubDocsScraper):
    repo = "keycloak/keycloak"
    branch = "main"
    source = "keycloak"
    version = "25"
    language = "java"
    topics_prefix = "keycloak,oauth,oidc"
    categories = "security,auth,identity"
    paths = ["README.md"]

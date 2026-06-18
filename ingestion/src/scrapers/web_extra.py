from .github_base import GitHubDocsScraper


class HonoScraper(GitHubDocsScraper):
    repo = "honojs/hono"
    branch = "main"
    source = "hono"
    version = "4"
    language = "typescript"
    topics_prefix = "hono,edge,http"
    categories = "web,typescript,rest,edge"
    paths = ["README.md"]


class FastifyScraper(GitHubDocsScraper):
    repo = "fastify/fastify"
    branch = "main"
    source = "fastify"
    version = "5"
    language = "javascript"
    topics_prefix = "fastify,node,http"
    categories = "web,javascript,rest"
    paths = [
        "README.md",
        "docs/Guides/Getting-Started.md",
        "docs/Guides/Plugins-Guide.md",
        "docs/Reference/Routes.md",
        "docs/Reference/Validation-and-Serialization.md",
    ]


class SymfonyScraper(GitHubDocsScraper):
    repo = "symfony/symfony"
    branch = "7.2"
    source = "symfony"
    version = "7.2"
    language = "php"
    topics_prefix = "symfony,php"
    categories = "web,php,fullstack"
    paths = ["README.md"]


class PhoenixScraper(GitHubDocsScraper):
    repo = "phoenixframework/phoenix"
    branch = "main"
    source = "phoenix"
    version = "1.7"
    language = "elixir"
    topics_prefix = "phoenix,elixir"
    categories = "web,elixir,fullstack,realtime"
    paths = [
        "guides/introduction/overview.md",
        "guides/introduction/installation.md",
        "guides/routing.md",
        "guides/controllers.md",
    ]


class ChiScraper(GitHubDocsScraper):
    repo = "go-chi/chi"
    branch = "master"
    source = "go-chi"
    version = "5"
    language = "go"
    topics_prefix = "chi,http,router"
    categories = "web,go,rest"
    paths = ["README.md"]


class GorillaMuxScraper(GitHubDocsScraper):
    repo = "gorilla/mux"
    branch = "main"
    source = "gorilla-mux"
    version = "1.8"
    language = "go"
    topics_prefix = "gorilla,mux,http"
    categories = "web,go,rest"
    paths = ["README.md"]


class SinatraScraper(GitHubDocsScraper):
    repo = "sinatra/sinatra"
    branch = "main"
    source = "sinatra"
    version = "4"
    language = "ruby"
    topics_prefix = "sinatra,ruby"
    categories = "web,ruby,rest"
    paths = ["README.md"]


class VertxScraper(GitHubDocsScraper):
    repo = "eclipse-vertx/vert.x"
    branch = "master"
    source = "vertx"
    version = "4.5"
    language = "java"
    topics_prefix = "vertx,reactive,java"
    categories = "web,java,reactive,event-driven"
    paths = ["README.md"]


class WarpScraper(GitHubDocsScraper):
    repo = "seanmonstar/warp"
    branch = "master"
    source = "warp"
    version = "0.3"
    language = "rust"
    topics_prefix = "warp,http,async"
    categories = "web,rust,rest,async"
    paths = ["README.md"]

# docpilot

MCP server providing semantic documentation search across 80+ frameworks and technologies. Packaged as a single Docker image — zero installation beyond Docker.

## Why?

AI coding agents like Claude Code, GitHub Copilot, Cursor, Windsurf, and JetBrains AI are already capable of generating code, fixing bugs, and refactoring entire modules. But they become much more effective when they have context about the framework you're using: that Spring Boot's `@CacheEvict` needs `@EnableCaching` on the config class, that Fiber middleware runs in registration order, that Django's `QuerySet` is lazy until evaluated, that Kubernetes Services need matching label selectors.

**docpilot** gives agents exactly that context. It is a standalone MCP server that lets any compatible AI agent search real, up-to-date documentation across 80+ frameworks and technologies — providing accurate API references, configuration patterns, and best practices instead of hallucinated code.

```
You:     "Add Redis caching to my Spring Boot service"
Agent:   (queries docpilot → gets Spring Boot caching docs + Redis config)
Result:  Correct @EnableCaching setup with RedisTemplate, not hallucinated code
```

Without docpilot, agents guess. With docpilot, they **know**.

## What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that lets AI agents discover and use tools exposed by external servers. Instead of hard-coding integrations for every framework, an agent connects to MCP servers that provide domain-specific capabilities. The agent discovers available tools at runtime and calls them as needed.

It's a plugin system for AI agents: connect to a server and the agent gains new capabilities.

docpilot exposes two tools via MCP:
- **`searchDocs`** — semantic search across all indexed documentation
- **`listFrameworks`** — discover what frameworks and technologies are available

## Documentation

📖 **[Full Documentation](https://shkna1368.github.io/docpilot/)**

## Quick Start

```bash
# Claude Code
claude mcp add framework-docs -- docker run -i --rm ghcr.io/shkna1368/docpilot:latest

# Kiro (~/.kiro/settings/mcp.json)
{
  "mcpServers": {
    "framework-docs": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}

# VS Code / Copilot (.vscode/mcp.json)
{
  "servers": {
    "framework-docs": {
      "type": "stdio",
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}

# Cursor / Windsurf / JetBrains
{
  "mcpServers": {
    "framework-docs": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}
```

## Supported Frameworks & Technologies

| Language | Frameworks |
|----------|-----------|
| Go | Fiber, Gin, Echo, Chi, Gorilla Mux |
| Java | Spring Boot, Spring Framework, Spring Security, Spring Data, Spring Cloud, Quarkus, Micronaut, Vert.x, Hibernate |
| Python | FastAPI, Django, Flask |
| Rust | Rocket, Actix-web, Axum, Warp |
| TypeScript | NestJS, Angular, Next.js, Nuxt.js, Hono |
| JavaScript | Express, React, Fastify |
| C# | ASP.NET Core |
| PHP | Laravel, Symfony |
| Ruby | Rails, Sinatra |
| Elixir | Phoenix |
| Dart | Flutter |
| Kotlin | Android (Jetpack Compose) |
| Swift | iOS (SwiftUI) |
| Cross-platform | React Native |

| AI / ML | Framework |
|---------|-----------|
| LangChain | 0.3 |
| CrewAI | 0.80 |
| Spring AI | 1.0 |
| Hugging Face Transformers | 4.44 |
| PyTorch | 2.4 |
| TensorFlow | 2.17 |
| Apache Spark | 3.5 |
| LlamaIndex | 0.11 |
| OpenAI API | 1.0 |
| Anthropic API | 1.0 |
| scikit-learn | 1.5 |
| MLflow | 2.16 |

| Technology | Version |
|-----------|---------|
| PostgreSQL | 17 |
| MySQL | 8 |
| Redis | 7 |
| MongoDB | 7 |
| Elasticsearch | 8 |
| Apache Kafka | 3.9 |
| RabbitMQ | 3.13 |
| NATS | 2.10 |
| gRPC | 1.60 |
| GraphQL | Oct2021 |
| Docker | 27 |
| Docker Compose | 2 |
| Kubernetes | 1.31 |
| Terraform | 1.9 |
| Pulumi | 3 |
| Jenkins | 2.4 |
| Helm | 3.16 |
| ArgoCD | 2.12 |
| Nginx | 1.27 |
| Traefik | 3 |
| Envoy | 1.31 |
| Istio | 1.23 |
| OpenTelemetry | 1.0 |
| Prometheus | 2.54 |
| Grafana | 11 |
| Vault | 1.17 |
| Keycloak | 25 |
| Git | 2 |

## Tools

### `searchDocs`

```
query:            "fiber route parameters"    # Natural-language query
framework:        "go-fiber"                  # Optional filter
frameworkVersion:  "3.3"                      # Optional version filter
projectDir:       "/path/to/project"          # Auto-detect framework
maxResults:       4                           # Default: 4, max: 50
```

Auto-detects your framework from project files (`go.mod`, `pom.xml`, `package.json`, `Cargo.toml`, etc.) and boosts relevant results.

### `listFrameworks`

Returns all indexed frameworks and technologies with their IDs, languages, and versions.

## Architecture

Single Docker container running:
- **PostgreSQL 17 + pgvector** — stores 15,000+ doc chunks with 384-dim embeddings
- **Quarkus MCP Server (Java 25)** — stdio transport, BGE Small EN v1.5 embedding model
- **ivfflat cosine index** — ~15ms average query latency

## Build from Source

**Requirements:** Java 25, Python 3.12+, Docker

```bash
# 1. Scrape and embed docs
cd ingestion
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
python -m src.cli scrape-all

# 2. Build MCP server
cd ..
./mvnw package -DskipTests -Dquarkus.package.jar.type=uber-jar

# 3. Build Docker image
docker build -t framework-docs-mcp:latest .

# 4. Test
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","method":"notifications/initialized"}\n{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"searchDocs","arguments":{"query":"fiber routing"}}}\n' \
  | docker run -i --rm framework-docs-mcp:latest
```

## Native Image Build (Optional)

For faster startup (~2s vs ~8s), build a native image:

```bash
./mvnw package -DskipTests -Dnative
docker build -f Dockerfile.native -t framework-docs-mcp:native .
```

Requires GraalVM 25+ with native-image installed.

## Project Structure

```
docpilot/
├── pom.xml                          # Quarkus + langchain4j + MCP
├── Dockerfile
├── Dockerfile.native                # GraalVM native image
├── docker/
│   ├── entrypoint.sh                # Starts PG then Java server
│   ├── init.sql                     # Schema (pgvector)
│   └── zz-index.sql                 # ivfflat index (after data load)
├── src/main/java/io/frameworkdocs/mcp/
│   ├── DocSearchTools.java          # MCP searchDocs + listFrameworks tools
│   ├── FrameworkDetector.java       # Auto-detect from project files
│   ├── EmbeddingModelLoader.java    # BGE model (async load)
│   ├── ContainerManager.java        # PgVector connection
│   ├── SqlLoader.java               # Schema readiness check
│   └── StartupObserver.java         # Warm-up on start
├── ingestion/
│   ├── pyproject.toml
│   ├── src/
│   │   ├── cli.py                   # scrape / scrape-all commands
│   │   ├── scraper.py               # DocPage + BaseScraper
│   │   ├── chunker.py               # Header-aware recursive split
│   │   ├── embedder.py              # BGE Small EN v1.5
│   │   ├── sql_writer.py            # INSERT statement generator
│   │   └── scrapers/                # One per framework (GitHub raw fetch)
│   ├── output/                      # Generated .sql files
│   └── tests/                       # Unit tests
└── .github/workflows/build.yml      # CI/CD pipeline
```

## How It Works

1. **Ingestion** (build time): Python fetches markdown/asciidoc from GitHub repos → splits by headers → embeds with BGE Small EN v1.5 → generates SQL INSERT statements
2. **Docker build**: Copies SQL files into PostgreSQL init directory
3. **First start**: PostgreSQL loads all SQL files (~10s), creates ivfflat index
4. **Runtime**: AI agent sends query → Quarkus embeds it → pgvector cosine similarity search → metadata boosting (title/topics/framework match) → returns ranked results

## Configuration

Environment variables (set in `application.properties`):

| Key | Default | Description |
|-----|---------|-------------|
| `docs-mcp.min-score` | 0.70 | Minimum cosine similarity |
| `docs-mcp.max-candidates` | 50 | Candidates before reranking |
| `docs-mcp.default-max-results` | 4 | Default results returned |

## Adding a New Framework

1. Create `ingestion/src/scrapers/my_framework.py`:
```python
from .github_base import GitHubDocsScraper

class MyFrameworkScraper(GitHubDocsScraper):
    repo = "org/repo"
    branch = "main"
    source = "my-framework"
    version = "1.0"
    language = "python"
    topics_prefix = "myframework"
    categories = "web,python"
    paths = ["docs/guide.md", "docs/api.md"]
```

2. Register in `ingestion/src/cli.py`
3. Run `python -m src.cli scrape --framework my-framework`
4. Rebuild Docker image

## License

MIT


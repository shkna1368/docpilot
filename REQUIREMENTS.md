# PRD: Multi-Framework Documentation Search MCP Server

## 1. Product Summary

**Product Name:** `framework-docs-mcp`

**One-liner:** A standalone MCP server that provides semantic documentation search across 16 web frameworks and their ecosystems, delivered as a single Docker image requiring zero installation beyond Docker.

**Problem:** AI agents lack reliable access to framework-specific documentation when generating code across polyglot microservice architectures. They hallucinate APIs, use deprecated patterns, and mix framework idioms.

**Solution:** An MCP server (Model Context Protocol) packaged as a Docker image containing the server, embedding model, and pre-indexed documentation. Any AI agent connects via stdio to `docker run`. User prerequisite: Docker only.

**Reference Implementation:** Modeled after [`quarkus-agent-mcp/DocSearchTools.java`](https://github.com/quarkusio/quarkus-agent-mcp).

---

## 2. Distribution Model

### End User (Zero Install)

The user only needs **Docker**. Everything else is inside the image.

**Claude Code:**
```bash
claude mcp add framework-docs -- docker run -i --rm ghcr.io/<org>/framework-docs-mcp:latest
```

**VS Code / Copilot (.vscode/mcp.json):**
```json
{
  "servers": {
    "framework-docs": {
      "type": "stdio",
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/<org>/framework-docs-mcp:latest"]
    }
  }
}
```

**Cursor / Windsurf / JetBrains:**
```json
{
  "mcpServers": {
    "framework-docs": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/<org>/framework-docs-mcp:latest"]
    }
  }
}
```

### Developer (Build from Source)

Developers need: Java 25, Python 3.12+, Docker.

```bash
# 1. Scrape and embed docs
cd ingestion && python -m src.cli scrape-all

# 2. Build MCP server
./mvnw package -DskipTests -Dquarkus.package.jar.type=uber-jar

# 3. Build Docker image
docker build -t framework-docs-mcp:latest .

# 4. Test locally
docker run -i --rm framework-docs-mcp:latest
```

---

## 3. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│               AI Agent (Claude, Copilot, Cursor, etc.)       │
└──────────────────────────┬──────────────────────────────────┘
                           │ MCP stdio (docker run -i)
┌──────────────────────────▼──────────────────────────────────┐
│              Docker Container: framework-docs-mcp            │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │         Quarkus MCP Server (Java 25)                   │  │
│  │                                                        │  │
│  │  ┌─────────────┐  ┌────────────────┐  ┌────────────┐  │  │
│  │  │ searchDocs  │  │ Framework      │  │ BGE v1.5   │  │  │
│  │  │ Tool        │  │ Detector       │  │ Model      │  │  │
│  │  └──────┬──────┘  └────────────────┘  └─────┬──────┘  │  │
│  │         │                                     │        │  │
│  │  ┌──────▼─────────────────────────────────────▼─────┐  │  │
│  │  │         PgVector Embedding Store (JDBC)          │  │  │
│  │  └──────────────────────┬───────────────────────────┘  │  │
│  └─────────────────────────┼──────────────────────────────┘  │
│                            │                                  │
│  ┌─────────────────────────▼───────────────────────────────┐  │
│  │  PostgreSQL 17 + pgvector (embedded, same container)    │  │
│  │  Table: rag_documents | Index: ivfflat cosine           │  │
│  │  Pre-loaded: ~80k doc chunks across all frameworks      │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

**Key design:** Both the MCP server AND PostgreSQL run inside the same container. An entrypoint script starts PostgreSQL first, then the Java MCP server. This eliminates Docker Compose and networking complexity.

---

## 4. Documentation Sources

### 4.1 Frameworks

| ID | Framework | Version | Language | Docs URL |
|----|-----------|---------|----------|----------|
| `go-fiber` | Go Fiber | 3.3 | Go | https://docs.gofiber.io |
| `spring-boot` | Spring Boot | 4.0 | Java | https://docs.spring.io/spring-boot/reference/ |
| `quarkus` | Quarkus | 3.36 | Java | https://quarkus.io/guides/ |
| `aspnet-core` | ASP.NET Core | 10 | C# | https://learn.microsoft.com/aspnet/core |
| `fastapi` | FastAPI | 0.136 | Python | https://fastapi.tiangolo.com |
| `go-gin` | Go Gin | 1.12 | Go | https://gin-gonic.com/docs/ |
| `actix-web` | Actix-web | 4.13 | Rust | https://actix.rs/docs/ |
| `go-echo` | Go Echo | 5.1 | Go | https://echo.labstack.com/docs |
| `rocket` | Rocket | 0.6 | Rust | https://rocket.rs/guide/v0.6 |
| `nestjs` | NestJS | 11 | TypeScript | https://docs.nestjs.com |
| `django` | Django | 6.0 | Python | https://docs.djangoproject.com/en/6.0/ |
| `axum` | Axum | 0.8 | Rust | https://docs.rs/axum/0.8 |
| `express` | Express | 4.22 | JavaScript | https://expressjs.com/en/guide/ |
| `flask` | Flask | 3.1.3 | Python | https://flask.palletsprojects.com/en/3.1.x/ |
| `csharp-minimal-api` | C# Minimal API | 10 | C# | https://learn.microsoft.com/aspnet/core/fundamentals/minimal-apis |

### 4.2 Technologies

| ID | Technology | Docs URL |
|----|-----------|----------|
| `postgresql` | PostgreSQL 17 | https://www.postgresql.org/docs/17/ |
| `mysql` | MySQL 8 | https://dev.mysql.com/doc/refman/8.0/en/ |
| `redis` | Redis 7 | https://redis.io/docs/ |
| `oracle` | Oracle 23c | https://docs.oracle.com/en/database/ |
| `kafka` | Apache Kafka | https://kafka.apache.org/documentation/ |
| `grpc` | gRPC | https://grpc.io/docs/ |
| `graphql` | GraphQL | https://graphql.org/learn/ |
| `spring-framework` | Spring Framework 7 | https://docs.spring.io/spring-framework/reference/ |
| `spring-security` | Spring Security 7 | https://docs.spring.io/spring-security/reference/ |
| `spring-data` | Spring Data 2024 | https://docs.spring.io/spring-data/commons/reference/ |
| `spring-cloud` | Spring Cloud 2024 | https://docs.spring.io/spring-cloud/reference/ |

---

## 5. Technical Specification

### 5.1 MCP Server (Runtime)

**Language:** Java 25  
**Framework:** Quarkus 3.36  
**MCP Transport:** stdio via `quarkus-mcp-server-stdio`  
**Embedding Model:** BGE Small EN v1.5 quantized (384 dimensions, ONNX runtime)  
**Vector Store:** langchain4j-pgvector  

### 5.2 Project Structure

```
framework-docs-mcp/
├── pom.xml
├── Dockerfile
├── entrypoint.sh                    # Starts PostgreSQL then Java server
├── src/main/java/io/frameworkdocs/mcp/
│   ├── DocSearchTools.java          # MCP tool: searchDocs
│   ├── FrameworkDetector.java       # Detects framework from projectDir
│   ├── EmbeddingModelLoader.java    # Loads BGE model async at startup
│   ├── ContainerManager.java        # Connects to local PostgreSQL
│   ├── SqlLoader.java              # Ensures schema + data is loaded
│   └── StartupObserver.java        # Triggers warm-up
├── src/main/resources/
│   ├── application.properties
│   └── banner.txt
├── ingestion/                       # Python scraping pipeline
│   ├── pyproject.toml
│   ├── src/
│   │   ├── cli.py
│   │   ├── scraper.py
│   │   ├── scrapers/               # One per framework
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   └── sql_writer.py
│   └── output/                     # Generated .sql files
│       ├── go-fiber-3.3.sql
│       ├── spring-boot-4.0.sql
│       └── ...
└── src/test/java/...
```

### 5.3 Dependencies (pom.xml)

```xml
<properties>
    <maven.compiler.release>25</maven.compiler.release>
    <quarkus.platform.version>3.36.0</quarkus.platform.version>
    <quarkus-mcp-server.version>1.11.0</quarkus-mcp-server.version>
    <langchain4j.version>1.12.2-beta22</langchain4j.version>
</properties>

<dependencies>
    <dependency>
        <groupId>io.quarkiverse.mcp</groupId>
        <artifactId>quarkus-mcp-server-stdio</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-pgvector</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-embeddings-bge-small-en-v15-q</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-arc</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-jackson</artifactId>
    </dependency>
</dependencies>
```

### 5.4 Database Schema

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS rag_documents (
    embedding_id UUID PRIMARY KEY,
    embedding vector(384),
    text TEXT,
    metadata JSONB
);

CREATE INDEX IF NOT EXISTS idx_rag_embedding
    ON rag_documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

**Metadata per row:**
```json
{
  "source": "go-fiber",
  "version": "3.3",
  "language": "go",
  "title": "Routing",
  "section_title": "Route Parameters",
  "url": "https://docs.gofiber.io/guide/routing#route-parameters",
  "topics": "fiber,routing,http,parameters",
  "categories": "web,go,rest"
}
```

### 5.5 MCP Tool Definition

```java
@Tool(name = "searchDocs",
      description = "Search documentation for Go Fiber, Spring Boot, Quarkus, ASP.NET Core, "
          + "FastAPI, Go Gin, Actix-web, Go Echo, Rocket, NestJS, Django, Axum, Express, "
          + "Flask, C# Minimal API, PostgreSQL, MySQL, Redis, Oracle, Kafka, gRPC, GraphQL. "
          + "Use for ANY framework or technology question.")
ToolResponse searchDocs(
    @ToolArg(description = "Natural-language query. Examples: 'fiber middleware', "
        + "'fastapi dependency injection', 'kafka consumer spring boot'")
    String query,

    @ToolArg(description = "Max results (default: 4, max: 50)", required = false)
    Integer maxResults,

    @ToolArg(description = "Project directory for framework auto-detection", required = false)
    String projectDir,

    @ToolArg(description = "Explicit framework filter: go-fiber, spring-boot, quarkus, "
        + "aspnet-core, fastapi, go-gin, actix-web, go-echo, rocket, nestjs, django, "
        + "axum, express, flask, csharp-minimal-api, postgresql, mysql, redis, oracle, "
        + "kafka, grpc, graphql", required = false)
    String framework
)
```

### 5.6 Search Algorithm

```
1. Embed query → BGE Small EN v1.5 → 384-dim vector
2. Query pgvector: cosine similarity, top 50, min score 0.82
3. Filter junk (< 50 chars, TOC-only, navigation fragments)
4. If framework param or detected from projectDir → filter to that source
5. Apply metadata boosting:
   - Title matches query term: +0.15
   - Topics match: +0.15
   - Section title matches: +0.08
   - URL path matches: +0.10
   - Detected framework matches result: +0.20
6. Apply synonym expansion
7. Sort by final score, return top N as JSON
```

### 5.7 Framework Detection

```java
public static String detect(String projectDir) {
    Path dir = Path.of(projectDir);

    // Go
    String goMod = readIfExists(dir.resolve("go.mod"));
    if (goMod != null) {
        if (goMod.contains("github.com/gofiber/fiber")) return "go-fiber";
        if (goMod.contains("github.com/gin-gonic/gin")) return "go-gin";
        if (goMod.contains("github.com/labstack/echo")) return "go-echo";
    }
    // Java
    String pom = readIfExists(dir.resolve("pom.xml"));
    if (pom != null) {
        if (pom.contains("spring-boot")) return "spring-boot";
        if (pom.contains("quarkus")) return "quarkus";
    }
    // C#
    Path csproj = findFirst(dir, "*.csproj");
    if (csproj != null && read(csproj).contains("Microsoft.AspNetCore")) return "aspnet-core";
    // Python
    String py = readIfExists(dir.resolve("requirements.txt"));
    if (py == null) py = readIfExists(dir.resolve("pyproject.toml"));
    if (py != null) {
        if (py.contains("fastapi")) return "fastapi";
        if (py.contains("django")) return "django";
        if (py.contains("flask")) return "flask";
    }
    // Rust
    String cargo = readIfExists(dir.resolve("Cargo.toml"));
    if (cargo != null) {
        if (cargo.contains("actix-web")) return "actix-web";
        if (cargo.contains("rocket")) return "rocket";
        if (cargo.contains("axum")) return "axum";
    }
    // Node.js
    String pkg = readIfExists(dir.resolve("package.json"));
    if (pkg != null) {
        if (pkg.contains("@nestjs/core")) return "nestjs";
        if (pkg.contains("\"express\"")) return "express";
    }
    return null;
}
```

### 5.8 Synonyms Map

```java
Map<String, String> SYNONYMS = Map.ofEntries(
    Map.entry("middleware", "handler"),
    Map.entry("endpoint", "route"),
    Map.entry("controller", "handler"),
    Map.entry("ORM", "database"),
    Map.entry("auth", "authentication"),
    Map.entry("di", "dependency injection"),
    Map.entry("test", "testing"),
    Map.entry("deploy", "deployment"),
    Map.entry("config", "configuration"),
    Map.entry("websocket", "ws"),
    Map.entry("stream", "kafka"),
    Map.entry("consumer", "kafka"),
    Map.entry("producer", "kafka"),
    Map.entry("proto", "grpc"),
    Map.entry("schema", "graphql"),
    Map.entry("cache", "redis"),
    Map.entry("query", "sql")
);
```

---

## 6. Ingestion Pipeline

### 6.1 Tech Stack

**Language:** Python 3.12+  
**Dependencies:**
```toml
[project]
name = "framework-docs-ingestion"
version = "1.0.0"
requires-python = ">=3.12"
dependencies = [
    "beautifulsoup4>=4.12",
    "httpx>=0.27",
    "sentence-transformers>=3.0",
    "langchain-text-splitters>=0.2",
    "click>=8.1",
]
```

### 6.2 Scraper Base

```python
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class DocPage:
    url: str
    title: str
    section_title: str
    text: str
    source: str       # "go-fiber"
    version: str      # "3.3"
    language: str     # "go"
    topics: str       # "fiber,routing,http"
    categories: str   # "web,go,rest"

class BaseScraper(ABC):
    @abstractmethod
    def scrape(self) -> list[DocPage]: ...
```

### 6.3 Chunker

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50,
    separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " "]
)

def chunk_page(page: DocPage) -> list[tuple[str, dict]]:
    chunks = splitter.split_text(page.text)
    return [(chunk, {
        "source": page.source, "version": page.version,
        "language": page.language, "title": page.title,
        "section_title": page.section_title, "url": page.url,
        "topics": page.topics, "categories": page.categories,
    }) for chunk in chunks if len(chunk.strip()) >= 50]
```

### 6.4 Embedder

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def embed_texts(texts: list[str]) -> list[list[float]]:
    return model.encode(texts, normalize_embeddings=True).tolist()
```

### 6.5 SQL Writer

```python
import json, uuid

def generate_sql(chunks: list[tuple[str, list[float], dict]], output_path: str):
    with open(output_path, "w") as f:
        for text, embedding, metadata in chunks:
            eid = uuid.uuid4()
            emb = "[" + ",".join(f"{v:.8f}" for v in embedding) + "]"
            txt = text.replace("'", "''")
            meta = json.dumps(metadata).replace("'", "''")
            f.write(f"INSERT INTO rag_documents VALUES ('{eid}','{emb}','{txt}','{meta}');\n")
```

### 6.6 CLI

```python
# python -m src.cli scrape-all
# python -m src.cli scrape --framework go-fiber
```

---

## 7. Docker Packaging

### 7.1 Dockerfile (Single Container: MCP Server + PostgreSQL)

```dockerfile
FROM postgres:17 AS pgvector-base
RUN apt-get update && apt-get install -y postgresql-17-pgvector && rm -rf /var/lib/apt/lists/*

FROM pgvector-base AS final

# Install JRE
RUN apt-get update && apt-get install -y openjdk-25-jre-headless && rm -rf /var/lib/apt/lists/*

# PostgreSQL config
ENV POSTGRES_USER=docs
ENV POSTGRES_PASSWORD=docs
ENV POSTGRES_DB=frameworkdocs
ENV PGDATA=/var/lib/postgresql/data

# Copy schema
COPY docker/init.sql /docker-entrypoint-initdb.d/00-schema.sql

# Copy pre-generated doc embeddings
COPY ingestion/output/*.sql /docker-entrypoint-initdb.d/

# Copy MCP server JAR
COPY target/*-runner.jar /app/server.jar

# Copy entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5432

ENTRYPOINT ["/entrypoint.sh"]
```

### 7.2 entrypoint.sh

```bash
#!/bin/bash
set -e

# Start PostgreSQL in background
docker-entrypoint.sh postgres &
PG_PID=$!

# Wait for PostgreSQL to be ready
until pg_isready -U docs -d frameworkdocs -q; do
    sleep 1
done

# Run MCP server (stdio mode — reads stdin, writes stdout)
exec java -jar /app/server.jar
```

### 7.3 docker/init.sql

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS rag_documents (
    embedding_id UUID PRIMARY KEY,
    embedding vector(384),
    text TEXT,
    metadata JSONB
);
```

**Note:** The ivfflat index is created AFTER data is loaded (PostgreSQL init scripts run alphabetically, so `00-schema.sql` runs first, then `01-go-fiber-3.3.sql`, etc.). A final `zz-index.sql` creates the index:

```sql
-- docker/zz-index.sql (copied to /docker-entrypoint-initdb.d/)
CREATE INDEX IF NOT EXISTS idx_rag_embedding
    ON rag_documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

---

## 8. Configuration (application.properties)

```properties
quarkus.mcp.server.server-info.name=framework-docs
quarkus.mcp.server.server-info.description=Multi-framework documentation search

# Database connection (inside same container)
docs-mcp.pg-host=localhost
docs-mcp.pg-port=5432
docs-mcp.pg-user=docs
docs-mcp.pg-password=docs
docs-mcp.pg-database=frameworkdocs

# Search tuning
docs-mcp.min-score=0.82
docs-mcp.max-candidates=50
docs-mcp.default-max-results=4

# Logging (stdout is MCP transport)
quarkus.log.console.enabled=false
quarkus.log.level=INFO
```

---

## 9. Build Commands

```bash
# === DEVELOPER WORKFLOW ===

# 1. Run ingestion (scrape + embed + generate SQL)
cd ingestion
pip install -e .
python -m src.cli scrape-all        # all frameworks
python -m src.cli scrape --framework go-fiber  # single framework

# 2. Build MCP server JAR
cd ..
./mvnw package -DskipTests -Dquarkus.package.jar.type=uber-jar

# 3. Build Docker image
docker build -t framework-docs-mcp:latest .

# 4. Test locally
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"searchDocs","arguments":{"query":"fiber middleware"}}}' | docker run -i --rm framework-docs-mcp:latest

# 5. Push
docker push ghcr.io/<org>/framework-docs-mcp:latest
```

---

## 10. Testing

### Unit Tests
- `FrameworkDetector` identifies all 15 framework types from project files
- Search scoring applies correct boosts
- Synonym expansion works for all mapped terms
- Junk filtering removes short/TOC chunks

### Integration Tests
- End-to-end: query against test pgvector with sample data
- Each framework returns results for basic queries (routing, config, database)
- Framework filter narrows results correctly
- Auto-detection + boosting works

### Ingestion Tests
- Each scraper produces non-empty DocPage list
- Chunker never produces chunks < 50 chars
- Embedder output is 384 dimensions, normalized
- SQL writer produces valid INSERT statements
- Generated SQL loads without errors into pgvector

---

## 11. Acceptance Criteria

| # | Criterion | Verification |
|---|-----------|-------------|
| 1 | `searchDocs(query="fiber route handler")` returns Go Fiber routing docs | Manual test |
| 2 | `searchDocs(query="kafka consumer", framework="spring-boot")` returns Spring Kafka docs | Manual test |
| 3 | `searchDocs(query="gRPC server", projectDir="/rust-project")` boosts Rust results | Manual test |
| 4 | All 15 frameworks return results for "how to create an endpoint" | Automated test |
| 5 | Query latency < 500ms after warm-up | Benchmark |
| 6 | Docker image starts and serves first query within 30s | Timing test |
| 7 | Image size < 2GB | `docker images` check |
| 8 | Works with Claude Code, VS Code, Cursor via stdio | Manual test |

---

## 12. Milestones

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 1 | 1 week | Project scaffold: pom.xml, Dockerfile, entrypoint, ingestion skeleton |
| 2 | 1 week | Ingestion pipeline: 3 scrapers (Go Fiber, FastAPI, Spring Boot) + end-to-end |
| 3 | 2 weeks | All 15 framework scrapers + 7 technology scrapers |
| 4 | 1 week | MCP server: searchDocs tool with scoring, synonyms, framework detection |
| 5 | 3 days | Docker image build, push to GHCR, test with Claude Code |
| 6 | 3 days | CI/CD: GitHub Actions to rebuild image on doc updates |

---

## 13. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Doc site blocks scraping | No data for framework | Use GitHub source markdown (most frameworks have docs in repo) |
| Doc format changes | Broken scraper | Per-framework isolation; CI detects empty output |
| Embedding model mismatch | Bad results | Pin exact model (BGE Small EN v1.5) in both ingestion and runtime |
| Large Docker image | Slow pull | Multi-stage build; only include JRE not JDK; compress SQL |
| Framework releases new version | Stale docs | Versioned SQL; re-run ingestion for new version |
| PostgreSQL cold start in container | Slow first query | Pre-initialize DB in Docker build (not at runtime) |

---

## 14. Future Enhancements

- Add `listFrameworks` tool to show indexed frameworks and versions
- Support mounting a volume to add custom doc sources without rebuilding image
- Add `--framework-version` flag to search specific version docs
- Native image build for faster container startup
- Webhook to auto-rebuild when framework docs update

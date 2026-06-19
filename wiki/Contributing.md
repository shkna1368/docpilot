# Contributing

## Development Setup

### Requirements
- Java 25
- Python 3.12+
- Docker

### Build from Source

```bash
# 1. Ingestion pipeline
cd ingestion
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# 2. Scrape a single framework
python -m src.cli scrape --framework hibernate

# 3. Scrape all frameworks
python -m src.cli scrape-all

# 4. Build MCP server
cd ..
./mvnw package -DskipTests -Dquarkus.package.jar.type=uber-jar

# 5. Build Docker image
docker build -t framework-docs-mcp:latest .
```

### Testing

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n{"jsonrpc":"2.0","method":"notifications/initialized"}\n{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"searchDocs","arguments":{"query":"hibernate entity mapping"}}}\n' \
  | docker run -i --rm framework-docs-mcp:latest
```

## How to Contribute

1. **Add a framework** — See [Adding a New Framework](Adding-a-New-Framework.md)
2. **Improve existing scrapers** — Add more doc paths to cover missing topics
3. **Fix bugs** — Submit a PR with a description of the issue
4. **Improve search quality** — Tune chunking, embedding, or reranking logic

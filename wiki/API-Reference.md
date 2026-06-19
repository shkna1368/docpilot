# API Reference

docpilot exposes two MCP tools via stdio transport.

## `searchDocs`

Semantic search across all indexed documentation.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | ✅ | Natural-language search query |
| `framework` | string | ❌ | Filter by framework ID (e.g., `"go-fiber"`, `"spring-boot"`, `"hibernate"`) |
| `frameworkVersion` | string | ❌ | Filter by version (e.g., `"4.0"`, `"3.36"`) |
| `projectDir` | string | ❌ | Path to project directory for auto-detection |
| `maxResults` | integer | ❌ | Max results (default: 4, max: 50) |

### Framework Auto-Detection

When `projectDir` is provided, docpilot scans for project files to boost relevant results:

| File | Detected Framework |
|------|--------------------|
| `go.mod` | Go (Fiber/Gin/Echo based on imports) |
| `pom.xml` | Spring Boot / Quarkus |
| `build.gradle` | Spring Boot / Quarkus |
| `package.json` | NestJS / Express / React / Angular |
| `Cargo.toml` | Rocket / Actix / Axum |
| `requirements.txt` | FastAPI / Django / Flask |
| `*.csproj` | ASP.NET Core |

### Example

```json
{
  "name": "searchDocs",
  "arguments": {
    "query": "hibernate second level cache configuration",
    "framework": "hibernate",
    "maxResults": 5
  }
}
```

## `listFrameworks`

Returns all indexed frameworks with their IDs, languages, and versions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | — | — | No parameters |

### Example Response

```json
[
  {"id": "hibernate", "language": "Java", "version": "7.0"},
  {"id": "spring-boot", "language": "Java", "version": "4.0"},
  {"id": "go-fiber", "language": "Go", "version": "3.3"}
]
```

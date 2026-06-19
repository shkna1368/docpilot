# Configuration

## Environment Variables

| Key | Default | Description |
|-----|---------|-------------|
| `docs-mcp.min-score` | 0.70 | Minimum cosine similarity threshold |
| `docs-mcp.max-candidates` | 50 | Number of candidates before reranking |
| `docs-mcp.default-max-results` | 4 | Default results returned to agent |

These are set in `src/main/resources/application.properties`.

## Tuning Search Quality

### Lowering `min-score`
Set below 0.70 to return more results (useful for broad queries). Risk: lower relevance.

### Raising `max-candidates`
Increase to consider more documents before reranking. Marginally slower but may surface better matches for ambiguous queries.

### `default-max-results`
Controls how many results are returned when the agent doesn't specify `maxResults`. The agent can override this up to 50.

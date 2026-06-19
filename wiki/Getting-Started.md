# Getting Started

## Prerequisites

- Docker installed

## Installation

Add docpilot to your AI agent's MCP configuration:

### Claude Code
```bash
claude mcp add framework-docs -- docker run -i --rm ghcr.io/shkna1368/docpilot:latest
```

### Kiro (~/.kiro/settings/mcp.json)
```json
{
  "mcpServers": {
    "framework-docs": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}
```

### VS Code / Copilot (.vscode/mcp.json)
```json
{
  "servers": {
    "framework-docs": {
      "type": "stdio",
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}
```

### Cursor / Windsurf / JetBrains
```json
{
  "mcpServers": {
    "framework-docs": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "ghcr.io/shkna1368/docpilot:latest"]
    }
  }
}
```

## Verify

Once configured, ask your agent something like:

```
"How do I set up routing in Go Fiber?"
```

The agent will call `searchDocs` and return accurate, up-to-date documentation.

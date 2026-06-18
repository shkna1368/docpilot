#!/bin/bash
set -e

# Start PostgreSQL in background, redirect ALL output to stderr
# (stdout must be clean for MCP JSON-RPC protocol)
docker-entrypoint.sh postgres >&2 2>&1 &

# Wait for PostgreSQL to accept connections
until pg_isready -U docs -d frameworkdocs -q 2>/dev/null; do
    sleep 0.5
done

# Wait for data to be loaded
until psql -U docs -d frameworkdocs -tAc "SELECT count(*) FROM rag_documents;" 2>/dev/null | grep -q "^[1-9]"; do
    sleep 1
done

# Run MCP server (stdio mode - only this writes to stdout)
exec java -jar /app/server.jar

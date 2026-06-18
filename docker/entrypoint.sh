#!/bin/bash
set -e

# Start PostgreSQL in background (first start loads all SQL files from initdb.d/)
docker-entrypoint.sh postgres &

# Wait for PostgreSQL to be fully ready (including init script completion)
until pg_isready -U docs -d frameworkdocs -q; do
    sleep 0.5
done

# Wait for data to be loaded (init scripts finish after pg_isready)
until psql -U docs -d frameworkdocs -tAc "SELECT count(*) FROM rag_documents;" 2>/dev/null | grep -q "^[1-9]"; do
    sleep 1
done

# Run MCP server (stdio mode)
exec java -jar /app/server.jar

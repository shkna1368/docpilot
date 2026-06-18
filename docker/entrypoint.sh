#!/bin/bash
set -e

# Start PostgreSQL in background
docker-entrypoint.sh postgres &
PG_PID=$!

# Wait for PostgreSQL to be ready
until pg_isready -U docs -d frameworkdocs -q; do
    sleep 1
done

# Run MCP server (stdio mode)
exec java -jar /app/server.jar

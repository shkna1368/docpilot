#!/bin/bash
set -e

# Start PostgreSQL in background
docker-entrypoint.sh postgres &

# Wait for PostgreSQL to be ready
until pg_isready -U docs -d frameworkdocs -q; do
    sleep 0.5
done

# Run native MCP server (stdio mode)
exec /app/server

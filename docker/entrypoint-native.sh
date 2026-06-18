#!/bin/bash
set -e

# Start PostgreSQL as postgres user (data is pre-initialized)
su postgres -c "pg_ctl -D $PGDATA -o \"-c listen_addresses='localhost'\" -w start"

# Run native MCP server (stdio mode)
exec /app/server

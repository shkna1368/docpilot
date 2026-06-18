FROM postgres:17 AS pgvector-base
RUN apt-get update && apt-get install -y postgresql-17-pgvector && rm -rf /var/lib/apt/lists/*

FROM pgvector-base AS final

RUN apt-get update && apt-get install -y openjdk-25-jre-headless && rm -rf /var/lib/apt/lists/*

ENV POSTGRES_USER=docs
ENV POSTGRES_PASSWORD=docs
ENV POSTGRES_DB=frameworkdocs
ENV PGDATA=/var/lib/postgresql/data

# Schema (runs first)
COPY docker/init.sql /docker-entrypoint-initdb.d/00-schema.sql

# Pre-generated SQL files per framework (inserted on first start)
COPY ingestion/output/*.sql /docker-entrypoint-initdb.d/

# Index (runs last)
COPY docker/zz-index.sql /docker-entrypoint-initdb.d/zz-index.sql

# MCP server
COPY target/*-runner.jar /app/server.jar

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

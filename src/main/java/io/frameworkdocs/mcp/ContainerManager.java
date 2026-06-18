package io.frameworkdocs.mcp;

import dev.langchain4j.store.embedding.pgvector.PgVectorEmbeddingStore;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.config.inject.ConfigProperty;

@ApplicationScoped
public class ContainerManager {

    @ConfigProperty(name = "docs-mcp.pg-host")
    String host;

    @ConfigProperty(name = "docs-mcp.pg-port")
    int port;

    @ConfigProperty(name = "docs-mcp.pg-user")
    String user;

    @ConfigProperty(name = "docs-mcp.pg-password")
    String password;

    @ConfigProperty(name = "docs-mcp.pg-database")
    String database;

    private volatile PgVectorEmbeddingStore store;

    public PgVectorEmbeddingStore getStore() {
        if (store == null) {
            synchronized (this) {
                if (store == null) {
                    store = PgVectorEmbeddingStore.builder()
                            .host(host)
                            .port(port)
                            .user(user)
                            .password(password)
                            .database(database)
                            .table("rag_documents")
                            .dimension(384)
                            .createTable(false)
                            .build();
                }
            }
        }
        return store;
    }
}

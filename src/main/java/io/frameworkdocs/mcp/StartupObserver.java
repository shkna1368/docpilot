package io.frameworkdocs.mcp;

import io.quarkus.runtime.StartupEvent;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.enterprise.event.Observes;
import jakarta.inject.Inject;
import org.jboss.logging.Logger;

@ApplicationScoped
public class StartupObserver {

    @Inject Logger log;
    @Inject EmbeddingModelLoader modelLoader;
    @Inject SqlLoader sqlLoader;

    void onStart(@Observes StartupEvent ev) {
        log.info("framework-docs-mcp starting...");
        if (sqlLoader.isSchemaReady()) {
            long count = sqlLoader.getDocumentCount();
            log.infof("Database ready: %d document chunks indexed", count);
        } else {
            log.warn("Database schema not ready - ensure PostgreSQL is initialized");
        }
        if (modelLoader.isReady()) {
            log.info("Embedding model loaded");
        } else {
            log.info("Embedding model loading in background...");
        }
    }
}

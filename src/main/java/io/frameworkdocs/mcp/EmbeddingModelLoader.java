package io.frameworkdocs.mcp;

import dev.langchain4j.model.embedding.EmbeddingModel;
import dev.langchain4j.model.embedding.onnx.bgesmallenv15q.BgeSmallEnV15QuantizedEmbeddingModel;
import io.quarkus.runtime.Startup;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.jboss.logging.Logger;

import java.util.concurrent.CompletableFuture;

@ApplicationScoped
@Startup
public class EmbeddingModelLoader {

    @Inject
    Logger log;

    private final CompletableFuture<EmbeddingModel> modelFuture;

    public EmbeddingModelLoader() {
        this.modelFuture = CompletableFuture.supplyAsync(() -> {
            var model = new BgeSmallEnV15QuantizedEmbeddingModel();
            return model;
        });
    }

    public EmbeddingModel getModel() {
        return modelFuture.join();
    }

    public boolean isReady() {
        return modelFuture.isDone() && !modelFuture.isCompletedExceptionally();
    }
}

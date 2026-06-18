package io.frameworkdocs.mcp;

import dev.langchain4j.data.embedding.Embedding;
import dev.langchain4j.data.segment.TextSegment;
import dev.langchain4j.store.embedding.EmbeddingMatch;
import dev.langchain4j.store.embedding.EmbeddingSearchRequest;
import io.quarkiverse.mcp.server.Tool;
import io.quarkiverse.mcp.server.ToolArg;
import io.quarkiverse.mcp.server.ToolResponse;
import io.quarkiverse.mcp.server.TextContent;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.config.inject.ConfigProperty;

import java.util.*;
import java.util.stream.Collectors;

@ApplicationScoped
public class DocSearchTools {

    private static final Map<String, String> SYNONYMS = Map.ofEntries(
            Map.entry("middleware", "handler"), Map.entry("endpoint", "route"),
            Map.entry("controller", "handler"), Map.entry("ORM", "database"),
            Map.entry("auth", "authentication"), Map.entry("di", "dependency injection"),
            Map.entry("test", "testing"), Map.entry("deploy", "deployment"),
            Map.entry("config", "configuration"), Map.entry("websocket", "ws"),
            Map.entry("stream", "kafka"), Map.entry("consumer", "kafka"),
            Map.entry("producer", "kafka"), Map.entry("proto", "grpc"),
            Map.entry("schema", "graphql"), Map.entry("cache", "redis"),
            Map.entry("query", "sql"));

    @Inject EmbeddingModelLoader modelLoader;
    @Inject ContainerManager containerManager;
    @Inject FrameworkDetector frameworkDetector;

    @ConfigProperty(name = "docs-mcp.min-score") double minScore;
    @ConfigProperty(name = "docs-mcp.max-candidates") int maxCandidates;
    @ConfigProperty(name = "docs-mcp.default-max-results") int defaultMaxResults;

    @Tool(name = "searchDocs", description = "Search documentation for Go Fiber, Spring Boot, Spring Framework, Spring Security, "
            + "Spring Data, Spring Cloud, Quarkus, ASP.NET Core, FastAPI, Go Gin, Actix-web, Go Echo, Rocket, NestJS, "
            + "Django, Axum, Express, Flask, C# Minimal API, PostgreSQL, MySQL, Redis, Oracle, Kafka, gRPC, GraphQL. "
            + "Use for ANY framework or technology question.")
    public ToolResponse searchDocs(
            @ToolArg(description = "Natural-language query") String query,
            @ToolArg(description = "Max results (default: 4, max: 50)", required = false) Integer maxResults,
            @ToolArg(description = "Project directory for framework auto-detection", required = false) String projectDir,
            @ToolArg(description = "Explicit framework filter: go-fiber, spring-boot, spring-framework, spring-security, spring-data, spring-cloud, quarkus, aspnet-core, fastapi, go-gin, actix-web, go-echo, rocket, nestjs, django, axum, express, flask, csharp-minimal-api, postgresql, mysql, redis, oracle, kafka, grpc, graphql", required = false) String framework) {

        int limit = (maxResults != null && maxResults > 0) ? Math.min(maxResults, 50) : defaultMaxResults;

        // Expand query with synonyms
        String expandedQuery = expandWithSynonyms(query);

        // Detect framework from project if not explicitly set
        String detectedFramework = framework;
        if (detectedFramework == null && projectDir != null) {
            detectedFramework = frameworkDetector.detect(projectDir);
        }

        // Embed query
        Embedding queryEmbedding = modelLoader.getModel().embed(expandedQuery).content();

        // Search pgvector
        var results = containerManager.getStore().search(
                EmbeddingSearchRequest.builder()
                        .queryEmbedding(queryEmbedding)
                        .maxResults(maxCandidates)
                        .minScore(minScore)
                        .build());

        // Score, filter, rank
        List<ScoredResult> scored = new ArrayList<>();
        String queryLower = query.toLowerCase();

        for (EmbeddingMatch<TextSegment> match : results.matches()) {
            TextSegment segment = match.embedded();
            if (segment == null) continue;
            String text = segment.text();
            if (text.length() < 50) continue; // junk filter

            var meta = segment.metadata().toMap();
            String source = str(meta, "source");
            String title = str(meta, "title").toLowerCase();
            String topics = str(meta, "topics").toLowerCase();
            String sectionTitle = str(meta, "section_title").toLowerCase();
            String url = str(meta, "url").toLowerCase();

            // Framework filter
            if (detectedFramework != null && !source.equals(detectedFramework)) continue;

            // Metadata boosting
            double score = match.score();
            if (title.contains(queryLower)) score += 0.15;
            if (topics.contains(queryLower)) score += 0.15;
            if (sectionTitle.contains(queryLower)) score += 0.08;
            if (url.contains(queryLower.replace(" ", "-"))) score += 0.10;
            if (detectedFramework != null && source.equals(detectedFramework)) score += 0.20;

            scored.add(new ScoredResult(score, text, meta));
        }

        scored.sort(Comparator.comparingDouble(ScoredResult::score).reversed());
        var topResults = scored.stream().limit(limit).toList();

        if (topResults.isEmpty()) {
            return ToolResponse.success(List.of(new TextContent("No documentation found for: " + query)));
        }

        // Format response
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < topResults.size(); i++) {
            var r = topResults.get(i);
            sb.append("## Result %d (score: %.3f)\n".formatted(i + 1, r.score()));
            sb.append("**Source:** %s | **Title:** %s\n".formatted(
                    r.metadata().getOrDefault("source", ""), r.metadata().getOrDefault("title", "")));
            String url = str(r.metadata(), "url");
            if (!url.isEmpty()) sb.append("**URL:** %s\n".formatted(url));
            sb.append("\n").append(r.text()).append("\n\n---\n\n");
        }

        return ToolResponse.success(List.of(new TextContent(sb.toString().trim())));
    }

    private String expandWithSynonyms(String query) {
        String[] words = query.toLowerCase().split("\\s+");
        Set<String> expanded = new LinkedHashSet<>(List.of(words));
        for (String word : words) {
            String syn = SYNONYMS.get(word);
            if (syn != null) expanded.add(syn);
        }
        return String.join(" ", expanded);
    }

    private String str(Map<String, Object> meta, String key) {
        Object v = meta.get(key);
        return v != null ? v.toString() : "";
    }

    private record ScoredResult(double score, String text, Map<String, Object> metadata) {}
}

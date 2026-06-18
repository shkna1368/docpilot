package io.frameworkdocs.mcp;

import jakarta.enterprise.context.ApplicationScoped;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

@ApplicationScoped
public class FrameworkDetector {

    public String detect(String projectDir) {
        if (projectDir == null || projectDir.isBlank()) return null;
        Path dir = Path.of(projectDir);
        if (!Files.isDirectory(dir)) return null;

        // Go
        String goMod = readIfExists(dir.resolve("go.mod"));
        if (goMod != null) {
            if (goMod.contains("github.com/gofiber/fiber")) return "go-fiber";
            if (goMod.contains("github.com/gin-gonic/gin")) return "go-gin";
            if (goMod.contains("github.com/labstack/echo")) return "go-echo";
        }
        // Java
        String pom = readIfExists(dir.resolve("pom.xml"));
        if (pom != null) {
            if (pom.contains("spring-cloud")) return "spring-cloud";
            if (pom.contains("spring-security")) return "spring-security";
            if (pom.contains("spring-data")) return "spring-data";
            if (pom.contains("spring-boot")) return "spring-boot";
            if (pom.contains("spring-framework") || pom.contains("spring-context")) return "spring-framework";
            if (pom.contains("quarkus")) return "quarkus";
        }
        String gradle = readIfExists(dir.resolve("build.gradle"));
        if (gradle == null) gradle = readIfExists(dir.resolve("build.gradle.kts"));
        if (gradle != null) {
            if (gradle.contains("spring-cloud")) return "spring-cloud";
            if (gradle.contains("spring-security")) return "spring-security";
            if (gradle.contains("spring-data")) return "spring-data";
            if (gradle.contains("spring-boot")) return "spring-boot";
            if (gradle.contains("quarkus")) return "quarkus";
        }
        // C#
        try (var stream = Files.list(dir)) {
            var csproj = stream.filter(p -> p.toString().endsWith(".csproj")).findFirst().orElse(null);
            if (csproj != null) {
                String content = Files.readString(csproj);
                if (content.contains("Microsoft.AspNetCore")) return "aspnet-core";
            }
        } catch (IOException ignored) {}
        // Python
        String py = readIfExists(dir.resolve("requirements.txt"));
        if (py == null) py = readIfExists(dir.resolve("pyproject.toml"));
        if (py != null) {
            if (py.contains("fastapi")) return "fastapi";
            if (py.contains("django")) return "django";
            if (py.contains("flask")) return "flask";
        }
        // Rust
        String cargo = readIfExists(dir.resolve("Cargo.toml"));
        if (cargo != null) {
            if (cargo.contains("actix-web")) return "actix-web";
            if (cargo.contains("rocket")) return "rocket";
            if (cargo.contains("axum")) return "axum";
        }
        // Node.js
        String pkg = readIfExists(dir.resolve("package.json"));
        if (pkg != null) {
            if (pkg.contains("@nestjs/core")) return "nestjs";
            if (pkg.contains("\"express\"")) return "express";
        }
        return null;
    }

    private String readIfExists(Path path) {
        try {
            return Files.exists(path) ? Files.readString(path) : null;
        } catch (IOException e) {
            return null;
        }
    }
}

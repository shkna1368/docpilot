package io.frameworkdocs.mcp;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.config.inject.ConfigProperty;
import org.jboss.logging.Logger;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;

@ApplicationScoped
public class SqlLoader {

    @Inject
    Logger log;

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

    public boolean isSchemaReady() {
        try (Connection conn = getConnection()) {
            ResultSet rs = conn.createStatement().executeQuery(
                    "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'rag_documents')");
            rs.next();
            return rs.getBoolean(1);
        } catch (Exception e) {
            log.warn("Schema check failed", e);
            return false;
        }
    }

    public long getDocumentCount() {
        try (Connection conn = getConnection()) {
            ResultSet rs = conn.createStatement().executeQuery("SELECT count(*) FROM rag_documents");
            rs.next();
            return rs.getLong(1);
        } catch (Exception e) {
            return 0;
        }
    }

    private Connection getConnection() throws Exception {
        return DriverManager.getConnection(
                "jdbc:postgresql://%s:%d/%s".formatted(host, port, database), user, password);
    }
}

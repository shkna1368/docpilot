"""Python port of FrameworkDetector logic for unit testing."""
import os
import tempfile


def detect(project_dir: str) -> str | None:
    """Port of Java FrameworkDetector.detect()."""
    if not project_dir or not os.path.isdir(project_dir):
        return None

    go_mod = _read(project_dir, "go.mod")
    if go_mod:
        if "github.com/gofiber/fiber" in go_mod: return "go-fiber"
        if "github.com/gin-gonic/gin" in go_mod: return "go-gin"
        if "github.com/labstack/echo" in go_mod: return "go-echo"

    pom = _read(project_dir, "pom.xml")
    if pom:
        if "spring-cloud" in pom: return "spring-cloud"
        if "spring-security" in pom: return "spring-security"
        if "spring-data" in pom: return "spring-data"
        if "spring-boot" in pom: return "spring-boot"
        if "spring-framework" in pom or "spring-context" in pom: return "spring-framework"
        if "quarkus" in pom: return "quarkus"

    py = _read(project_dir, "requirements.txt") or _read(project_dir, "pyproject.toml")
    if py:
        if "fastapi" in py: return "fastapi"
        if "django" in py: return "django"
        if "flask" in py: return "flask"

    cargo = _read(project_dir, "Cargo.toml")
    if cargo:
        if "actix-web" in cargo: return "actix-web"
        if "rocket" in cargo: return "rocket"
        if "axum" in cargo: return "axum"

    pkg = _read(project_dir, "package.json")
    if pkg:
        if "@nestjs/core" in pkg: return "nestjs"
        if '"express"' in pkg: return "express"

    return None


def _read(directory: str, filename: str) -> str | None:
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        return open(path).read()
    return None


def _make_project(files: dict[str, str]) -> str:
    d = tempfile.mkdtemp()
    for name, content in files.items():
        with open(os.path.join(d, name), "w") as f:
            f.write(content)
    return d


def test_detect_go_fiber():
    d = _make_project({"go.mod": "module x\nrequire github.com/gofiber/fiber/v2 v2.50.0"})
    assert detect(d) == "go-fiber"


def test_detect_spring_boot():
    d = _make_project({"pom.xml": "<dependency>spring-boot-starter-web</dependency>"})
    assert detect(d) == "spring-boot"


def test_detect_fastapi():
    d = _make_project({"requirements.txt": "fastapi==0.100.0\nuvicorn"})
    assert detect(d) == "fastapi"


def test_detect_nestjs():
    d = _make_project({"package.json": '{"dependencies": {"@nestjs/core": "^10.0.0"}}'})
    assert detect(d) == "nestjs"


def test_detect_actix_web():
    d = _make_project({"Cargo.toml": '[dependencies]\nactix-web = "4"'})
    assert detect(d) == "actix-web"


def test_spring_security_before_spring_boot():
    d = _make_project({"pom.xml": "<deps>spring-security-config spring-boot-starter</deps>"})
    assert detect(d) == "spring-security"


def test_unknown_project():
    d = _make_project({"README.md": "just a readme"})
    assert detect(d) is None

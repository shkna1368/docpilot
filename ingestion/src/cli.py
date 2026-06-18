import click
from pathlib import Path
from .chunker import chunk_page
from .embedder import embed_texts
from .sql_writer import generate_sql

SCRAPERS = {}

def _register_scrapers():
    from .scrapers.go_fiber import GoFiberScraper
    from .scrapers.go_gin import GinScraper
    from .scrapers.go_echo import EchoScraper
    from .scrapers.fastapi import FastAPIScraper
    from .scrapers.express import ExpressScraper
    from .scrapers.nestjs import NestJSScraper
    from .scrapers.rocket import RocketScraper
    from .scrapers.actix_web import ActixWebScraper
    from .scrapers.django import DjangoScraper
    from .scrapers.flask import FlaskScraper
    from .scrapers.aspnet_core import AspNetCoreScraper
    from .scrapers.spring_boot import SpringBootScraper
    from .scrapers.spring_framework import SpringFrameworkScraper
    from .scrapers.spring_security import SpringSecurityScraper
    from .scrapers.spring_data import SpringDataScraper
    from .scrapers.spring_cloud import SpringCloudScraper
    from .scrapers.quarkus import QuarkusScraper
    from .scrapers.axum import AxumScraper
    from .scrapers.postgresql import PostgreSQLScraper
    from .scrapers.mysql import MySQLServerScraper, MySQLShellScraper, MySQLOperatorScraper, MySQLConnectorJScraper, MySQLConnectorPythonScraper
    from .scrapers.redis import RedisScraper, RedisDocScraper
    from .scrapers.kafka import KafkaScraper
    from .scrapers.grpc import GrpcScraper
    from .scrapers.graphql import GraphQLScraper
    from .scrapers.angular import AngularScraper
    from .scrapers.react import ReactScraper
    from .scrapers.docker import DockerScraper
    from .scrapers.kubernetes import KubernetesScraper
    from .scrapers.terraform import TerraformScraper
    from .scrapers.mongodb import MongoDBScraper
    from .scrapers.elasticsearch import ElasticsearchScraper
    from .scrapers.rabbitmq import RabbitMQScraper
    from .scrapers.jenkins import JenkinsScraper
    from .scrapers.flutter import FlutterScraper, FlutterSamplesScraper
    from .scrapers.react_native import ReactNativeScraper
    from .scrapers.android import AndroidScraper, AndroidComposeScraper, AndroidArchScraper
    from .scrapers.ios_swift import SwiftScraper
    from .scrapers.langchain import LangChainScraper
    from .scrapers.crewai import CrewAIScraper
    from .scrapers.pytorch import PyTorchScraper
    from .scrapers.tensorflow import TensorFlowScraper
    from .scrapers.transformers import TransformersScraper
    from .scrapers.spring_ai import SpringAIScraper
    from .scrapers.spark import SparkScraper
    from .scrapers.nextjs import NextJSScraper
    from .scrapers.nuxtjs import NuxtScraper
    from .scrapers.laravel import LaravelScraper
    from .scrapers.rails import RailsScraper
    from .scrapers.micronaut import MicronautScraper
    from .scrapers.opentelemetry import OpenTelemetryScraper
    from .scrapers.helm import HelmScraper
    from .scrapers.nginx import NginxScraper
    from .scrapers.llm_apis import OpenAIScraper, AnthropicScraper
    from .scrapers.llamaindex import LlamaIndexScraper
    from .scrapers.observability import PrometheusScraper, GrafanaScraper, VaultScraper
    from .scrapers.web_extra import HonoScraper, FastifyScraper, SymfonyScraper, PhoenixScraper, ChiScraper, GorillaMuxScraper, SinatraScraper, VertxScraper, WarpScraper
    from .scrapers.infra_extra import TraefikScraper, EnvoyScraper, IstioScraper, ArgoCDScraper, PulumiScraper, KeycloakScraper
    from .scrapers.ml_extra import ScikitLearnScraper, MLflowScraper
    from .scrapers.nats import NATSScraper
    from .scrapers.kafka_clients import KafkaPythonScraper, KafkaGoScraper, KafkaRustScraper
    from .scrapers.go_ecosystem import GoRedisScraper, PgxScraper, GrpcGoScraper, SqlcScraper
    from .scrapers.rust_ecosystem import SqlxScraper, TonicScraper, SeaOrmScraper
    from .scrapers.oracle import OracleGoScraper, OracleNodeScraper, OraclePythonScraper
    SCRAPERS["go-fiber"] = GoFiberScraper()
    SCRAPERS["go-gin"] = GinScraper()
    SCRAPERS["go-echo"] = EchoScraper()
    SCRAPERS["fastapi"] = FastAPIScraper()
    SCRAPERS["express"] = ExpressScraper()
    SCRAPERS["nestjs"] = NestJSScraper()
    SCRAPERS["rocket"] = RocketScraper()
    SCRAPERS["actix-web"] = ActixWebScraper()
    SCRAPERS["django"] = DjangoScraper()
    SCRAPERS["flask"] = FlaskScraper()
    SCRAPERS["aspnet-core"] = AspNetCoreScraper()
    SCRAPERS["spring-boot"] = SpringBootScraper()
    SCRAPERS["spring-framework"] = SpringFrameworkScraper()
    SCRAPERS["spring-security"] = SpringSecurityScraper()
    SCRAPERS["spring-data"] = SpringDataScraper()
    SCRAPERS["spring-cloud"] = SpringCloudScraper()
    SCRAPERS["quarkus"] = QuarkusScraper()
    SCRAPERS["axum"] = AxumScraper()
    SCRAPERS["postgresql"] = PostgreSQLScraper()
    SCRAPERS["mysql"] = MySQLServerScraper()
    SCRAPERS["mysql-shell"] = MySQLShellScraper()
    SCRAPERS["mysql-operator"] = MySQLOperatorScraper()
    SCRAPERS["mysql-connector-j"] = MySQLConnectorJScraper()
    SCRAPERS["mysql-connector-python"] = MySQLConnectorPythonScraper()
    SCRAPERS["redis"] = RedisScraper()
    SCRAPERS["redis-doc"] = RedisDocScraper()
    SCRAPERS["kafka"] = KafkaScraper()
    SCRAPERS["grpc"] = GrpcScraper()
    SCRAPERS["graphql"] = GraphQLScraper()
    SCRAPERS["angular"] = AngularScraper()
    SCRAPERS["react"] = ReactScraper()
    SCRAPERS["docker"] = DockerScraper()
    SCRAPERS["kubernetes"] = KubernetesScraper()
    SCRAPERS["terraform"] = TerraformScraper()
    SCRAPERS["mongodb"] = MongoDBScraper()
    SCRAPERS["elasticsearch"] = ElasticsearchScraper()
    SCRAPERS["rabbitmq"] = RabbitMQScraper()
    SCRAPERS["jenkins"] = JenkinsScraper()
    SCRAPERS["flutter"] = FlutterScraper()
    SCRAPERS["flutter-samples"] = FlutterSamplesScraper()
    SCRAPERS["react-native"] = ReactNativeScraper()
    SCRAPERS["android"] = AndroidScraper()
    SCRAPERS["android-compose"] = AndroidComposeScraper()
    SCRAPERS["android-arch"] = AndroidArchScraper()
    SCRAPERS["ios-swift"] = SwiftScraper()
    SCRAPERS["langchain"] = LangChainScraper()
    SCRAPERS["crewai"] = CrewAIScraper()
    SCRAPERS["pytorch"] = PyTorchScraper()
    SCRAPERS["tensorflow"] = TensorFlowScraper()
    SCRAPERS["transformers"] = TransformersScraper()
    SCRAPERS["spring-ai"] = SpringAIScraper()
    SCRAPERS["spark"] = SparkScraper()
    SCRAPERS["nextjs"] = NextJSScraper()
    SCRAPERS["nuxtjs"] = NuxtScraper()
    SCRAPERS["laravel"] = LaravelScraper()
    SCRAPERS["rails"] = RailsScraper()
    SCRAPERS["micronaut"] = MicronautScraper()
    SCRAPERS["opentelemetry"] = OpenTelemetryScraper()
    SCRAPERS["helm"] = HelmScraper()
    SCRAPERS["nginx"] = NginxScraper()
    SCRAPERS["openai"] = OpenAIScraper()
    SCRAPERS["anthropic"] = AnthropicScraper()
    SCRAPERS["llamaindex"] = LlamaIndexScraper()
    SCRAPERS["prometheus"] = PrometheusScraper()
    SCRAPERS["grafana"] = GrafanaScraper()
    SCRAPERS["vault"] = VaultScraper()
    SCRAPERS["hono"] = HonoScraper()
    SCRAPERS["fastify"] = FastifyScraper()
    SCRAPERS["symfony"] = SymfonyScraper()
    SCRAPERS["phoenix"] = PhoenixScraper()
    SCRAPERS["go-chi"] = ChiScraper()
    SCRAPERS["gorilla-mux"] = GorillaMuxScraper()
    SCRAPERS["sinatra"] = SinatraScraper()
    SCRAPERS["vertx"] = VertxScraper()
    SCRAPERS["warp"] = WarpScraper()
    SCRAPERS["traefik"] = TraefikScraper()
    SCRAPERS["envoy"] = EnvoyScraper()
    SCRAPERS["istio"] = IstioScraper()
    SCRAPERS["argocd"] = ArgoCDScraper()
    SCRAPERS["pulumi"] = PulumiScraper()
    SCRAPERS["keycloak"] = KeycloakScraper()
    SCRAPERS["scikit-learn"] = ScikitLearnScraper()
    SCRAPERS["mlflow"] = MLflowScraper()
    SCRAPERS["nats"] = NATSScraper()
    SCRAPERS["kafka-python"] = KafkaPythonScraper()
    SCRAPERS["kafka-go"] = KafkaGoScraper()
    SCRAPERS["kafka-rust"] = KafkaRustScraper()
    SCRAPERS["go-redis"] = GoRedisScraper()
    SCRAPERS["pgx"] = PgxScraper()
    SCRAPERS["grpc-go"] = GrpcGoScraper()
    SCRAPERS["sqlc"] = SqlcScraper()
    SCRAPERS["sqlx"] = SqlxScraper()
    SCRAPERS["tonic"] = TonicScraper()
    SCRAPERS["sea-orm"] = SeaOrmScraper()
    SCRAPERS["oracle-go"] = OracleGoScraper()
    SCRAPERS["oracle-node"] = OracleNodeScraper()
    SCRAPERS["oracle-python"] = OraclePythonScraper()


def _run_scraper(name: str, scraper):
    click.echo(f"Scraping {name}...")
    pages = scraper.scrape()
    click.echo(f"  {len(pages)} pages scraped")

    all_chunks = []
    for page in pages:
        all_chunks.extend(chunk_page(page))
    click.echo(f"  {len(all_chunks)} chunks created")

    texts = [c[0] for c in all_chunks]
    click.echo(f"  Embedding {len(texts)} chunks...")
    embeddings = embed_texts(texts)

    final = [(text, emb, meta) for (text, meta), emb in zip(all_chunks, embeddings)]

    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = str(output_dir / f"{name}-{pages[0].version if pages else '0'}.sql")
    generate_sql(final, output_path)
    click.echo(f"  Written to {output_path}")


@click.group()
def main():
    """Framework documentation ingestion pipeline."""
    pass


@main.command()
@click.option("--framework", required=True, help="Framework ID to scrape")
def scrape(framework: str):
    _register_scrapers()
    if framework not in SCRAPERS:
        click.echo(f"Unknown framework: {framework}. Available: {list(SCRAPERS.keys())}")
        return
    _run_scraper(framework, SCRAPERS[framework])


@main.command("scrape-all")
def scrape_all():
    _register_scrapers()
    for name, scraper in SCRAPERS.items():
        _run_scraper(name, scraper)


if __name__ == "__main__":
    main()

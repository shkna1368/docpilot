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
    from .scrapers.mysql import MySQLScraper
    from .scrapers.redis import RedisScraper
    from .scrapers.kafka import KafkaScraper
    from .scrapers.grpc import GrpcScraper
    from .scrapers.graphql import GraphQLScraper
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
    SCRAPERS["mysql"] = MySQLScraper()
    SCRAPERS["redis"] = RedisScraper()
    SCRAPERS["kafka"] = KafkaScraper()
    SCRAPERS["grpc"] = GrpcScraper()
    SCRAPERS["graphql"] = GraphQLScraper()


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

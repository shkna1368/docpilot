from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class DocPage:
    url: str
    title: str
    section_title: str
    text: str
    source: str
    version: str
    language: str
    topics: str
    categories: str


class BaseScraper(ABC):
    @abstractmethod
    def scrape(self) -> list[DocPage]: ...

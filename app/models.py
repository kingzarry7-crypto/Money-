from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Opportunity:
    title: str
    url: str
    source: str
    summary: str
    published: datetime | None = None
    category: str = "opportunity"


@dataclass(frozen=True)
class RankedOpportunity:
    opportunity: Opportunity
    relevance: int
    earning_potential: int
    effort: int
    freshness: int

    @property
    def total(self) -> int:
        return self.relevance + self.earning_potential + self.effort + self.freshness

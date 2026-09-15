from datetime import datetime, timezone
from .models import Opportunity, RankedOpportunity


def _keyword_score(text: str, keywords: list[str], cap: int = 10) -> int:
    lowered = text.lower()
    return min(cap, sum(2 for word in keywords if word.lower() in lowered))


def score(item: Opportunity, interests: list[str], now: datetime | None = None) -> RankedOpportunity:
    now = now or datetime.now(timezone.utc)
    text = f"{item.title} {item.summary}"
    relevance = min(10, 2 + _keyword_score(text, interests))
    money_terms = ["job", "contract", "freelance", "grant", "funding", "revenue", "business", "launch"]
    earning = min(10, 2 + _keyword_score(text, money_terms))
    effort = 6 if any(word in text.lower() for word in ["api", "github", "software", "automation"]) else 4
    freshness = 2
    if item.published:
        age_days = max(0, (now - item.published).days)
        freshness = max(0, 10 - min(10, age_days))
    return RankedOpportunity(item, relevance, earning, effort, freshness)


def rank(items: list[Opportunity], interests: list[str], now: datetime | None = None) -> list[RankedOpportunity]:
    return sorted((score(item, interests, now) for item in items), key=lambda x: x.total, reverse=True)

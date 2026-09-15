from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import feedparser
from .models import Opportunity


def _published(entry) -> datetime | None:
    value = entry.get("published") or entry.get("updated")
    if not value:
        return None
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def collect(feed_urls: list[str], limit_per_feed: int = 25) -> list[Opportunity]:
    items: list[Opportunity] = []
    for url in feed_urls:
        parsed = feedparser.parse(url)
        source = parsed.feed.get("title") or url
        for entry in parsed.entries[:limit_per_feed]:
            title = (entry.get("title") or "Untitled").strip()
            link = (entry.get("link") or "").strip()
            summary = (entry.get("summary") or entry.get("description") or "").strip()
            if link:
                items.append(Opportunity(title, link, source, summary[:500], _published(entry)))
    return items

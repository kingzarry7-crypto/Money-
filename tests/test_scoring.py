from datetime import datetime, timezone
from app.models import Opportunity
from app.scoring import score


def test_relevant_recent_item_scores_higher():
    now = datetime(2026, 9, 15, tzinfo=timezone.utc)
    item = Opportunity(
        title="AI automation freelance contract",
        url="https://example.com/item",
        source="Example",
        summary="Build a finance workflow with an API",
        published=now,
    )
    result = score(item, ["AI", "finance"], now)
    assert result.total >= 25
    assert result.freshness == 10

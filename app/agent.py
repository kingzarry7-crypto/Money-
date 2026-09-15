from datetime import datetime, timezone
from .models import RankedOpportunity
from .scoring import rank


def briefing(items, interests: list[str], location: str, max_items: int) -> str:
    ranked = rank(items, interests, datetime.now(timezone.utc))[:max_items]
    lines = [f"Opportunity briefing — {location}", ""]
    if not ranked:
        return "Opportunity briefing\n\nNo opportunities were found from the configured feeds."
    for index, item in enumerate(ranked, 1):
        opportunity = item.opportunity
        lines.extend([
            f"{index}. {opportunity.title}",
            f"Source: {opportunity.source}",
            f"Score: {item.total}/40 (relevance {item.relevance}, earning {item.earning_potential}, effort {item.effort}, freshness {item.freshness})",
            f"Why review it: {opportunity.summary or 'Open the source for details.'}",
            f"Link: {opportunity.url}",
            "",
        ])
    lines.append("Research only: verify details before applying, paying, trading, or contacting anyone.")
    return "\n".join(lines)

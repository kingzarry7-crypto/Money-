from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


def _csv(name: str, default: str = "") -> list[str]:
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    feed_urls: list[str]
    interests: list[str]
    location: str
    max_items: int
    telegram_bot_token: str | None
    telegram_chat_id: str | None


def settings() -> Settings:
    return Settings(
        feed_urls=_csv("FEED_URLS"),
        interests=_csv("INTERESTS"),
        location=os.getenv("LOCATION", "London, UK"),
        max_items=max(1, int(os.getenv("MAX_ITEMS", "5"))),
        telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN") or None,
        telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID") or None,
    )

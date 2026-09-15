import time
from typing import Any
import requests
from .agent import briefing
from .config import settings
from .sources import collect


HELP = (
    "Available commands:\n"
    "/briefing - Get the latest opportunity briefing\n"
    "/jobs - Show job-related opportunities\n"
    "/ideas - Show business and income ideas\n"
    "/releases - Show new product and AI releases\n"
    "/help - Show this help"
)


def api(token: str, method: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/{method}",
        json=payload or {},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    if not data.get("ok"):
        raise RuntimeError(data.get("description", "Telegram API error"))
    return data


def allowed(chat_id: int, configured_chat_id: str | None) -> bool:
    return not configured_chat_id or str(chat_id) == str(configured_chat_id)


def response_for(command: str, location: str, interests: list[str], feed_urls: list[str], max_items: int) -> str:
    items = collect(feed_urls)
    command = command.split()[0].lower().split("@")[0]
    if command in {"/start", "/help"}:
        return "Opportunity agent is online.\n\n" + HELP
    if command == "/briefing":
        return briefing(items, interests, location, max_items)
    if command == "/jobs":
        return briefing([item for item in items if any(word in (item.title + item.summary).lower() for word in ["job", "hire", "career", "contract", "freelance"])], interests, location, max_items)
    if command == "/ideas":
        return briefing([item for item in items if any(word in (item.title + item.summary).lower() for word in ["business", "startup", "revenue", "funding", "launch", "automation"])], interests, location, max_items)
    if command == "/releases":
        return briefing([item for item in items if any(word in (item.title + item.summary).lower() for word in ["release", "launch", "ai", "api", "software", "github"])], interests, location, max_items)
    return "I do not recognise that command. Send /help."


def run() -> None:
    config = settings()
    if not config.telegram_bot_token:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN before starting the Telegram service.")
    offset: int | None = None
    while True:
        data = api(config.telegram_bot_token, "getUpdates", {"timeout": 25, "offset": offset})
        for update in data.get("result", []):
            offset = update["update_id"] + 1
            message = update.get("message") or {}
            chat = message.get("chat") or {}
            text = (message.get("text") or "").strip()
            if not text or not chat.get("id") or not allowed(chat["id"], config.telegram_chat_id):
                continue
            try:
                reply = response_for(text, config.location, config.interests, config.feed_urls, config.max_items)
            except Exception as exc:
                reply = f"Agent error: {exc}"
            api(config.telegram_bot_token, "sendMessage", {"chat_id": chat["id"], "text": reply, "disable_web_page_preview": True})
        time.sleep(1)

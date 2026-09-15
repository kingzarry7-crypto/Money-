import argparse
import sys
from .agent import briefing
from .config import settings
from .sources import collect
from .telegram import send_message


def run(send_telegram: bool = False) -> str:
    config = settings()
    items = collect(config.feed_urls)
    report = briefing(items, config.interests, config.location, config.max_items)
    if send_telegram:
        if not config.telegram_bot_token or not config.telegram_chat_id:
            raise RuntimeError("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID before sending.")
        send_message(config.telegram_bot_token, config.telegram_chat_id, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only opportunity briefing worker")
    parser.add_argument("--send-telegram", action="store_true")
    args = parser.parse_args()
    try:
        print(run(args.send_telegram))
    except Exception as exc:
        print(f"Agent failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

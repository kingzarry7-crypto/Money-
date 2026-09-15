import argparse
from .agent import briefing
from .config import settings
from .sources import collect
from .telegram import send_message


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--send-telegram", action="store_true")
    args = parser.parse_args()
    config = settings()
    items = collect(config.feed_urls)
    report = briefing(items, config.interests, config.location, config.max_items)
    print(report)
    if args.send_telegram:
        if not config.telegram_bot_token or not config.telegram_chat_id:
            raise SystemExit("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID before sending.")
        send_message(config.telegram_bot_token, config.telegram_chat_id, report)


if __name__ == "__main__":
    main()

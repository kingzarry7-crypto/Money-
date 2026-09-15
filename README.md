# Opportunity Discovery Agent

A read-only worker that collects new opportunities from RSS/Atom feeds, ranks them transparently, and can send a briefing to Telegram. It does not apply for jobs, spend money, trade, publish content, or claim that an opportunity will make money.

## What it does

- Reads configurable RSS/Atom feeds.
- Extracts title, URL, source, and publication date.
- Scores relevance, earning potential, effort, and freshness using explicit rules.
- Produces a briefing.
- Optionally sends the briefing to Telegram.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.main
pytest
```

On Windows, activate with `.venv\\Scripts\\activate`.

## Telegram setup

1. Create a bot with Telegram's `@BotFather`.
2. Start a chat with the bot and send `/start`.
3. Find your chat ID using an approved Telegram update method.
4. Put `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in your deployment environment.
5. Run `python -m app.main --send-telegram`.

Keep the token secret. The agent only sends the generated briefing; it cannot apply, purchase, trade, or message other recipients.

## Railway deployment

This repository is a one-shot worker, not a web server. `railway.toml` tells Railway to build with Nixpacks and run:

```bash
python -m app.main --send-telegram
```

Set these variables in Railway:

```text
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
FEED_URLS=https://hnrss.org/newest,https://github.blog/feed/
LOCATION=London, UK
INTERESTS=AI automation,finance technology,software,remote work
MAX_ITEMS=5
```

The worker exits after each run. Configure it as a scheduled/cron execution if your Railway plan supports scheduled jobs. Do not use restart-on-failure as the schedule; the process should run once per scheduled invocation.

The logs may say `Stopping Container` after a successful run. That is expected for a one-shot worker. A successful run should show `Opportunity briefing` and exit code 0. A failed run prints `Agent failed: ...` and exits with code 1.

## Planned next steps

- Add source-specific adapters for job boards and official release feeds.
- Add SQLite/Postgres deduplication.
- Add an optional model step for explanations, with citations preserved.
- Add Telegram commands such as `/jobs`, `/ideas`, `/save`, and `/ignore`.
- Add human approval before drafting applications or contacting anyone.

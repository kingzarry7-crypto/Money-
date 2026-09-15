# Opportunity Discovery Agent

A read-only starter agent that collects new opportunities from RSS/Atom feeds, ranks them transparently, and can send a briefing to Telegram. It does not apply for jobs, spend money, trade, publish content, or claim that an opportunity will make money.

## What it does

- Reads configurable RSS/Atom feeds.
- Extracts title, URL, source, and publication date.
- Scores relevance, earning potential, effort, and freshness using explicit rules.
- Produces a Markdown briefing.
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
4. Put `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `.env`.
5. Run `python -m app.main --send-telegram`.

Keep the token secret. The agent only sends the generated briefing; it cannot apply, purchase, trade, or message other recipients.

## Configuration

`FEED_URLS` is a comma-separated list of trusted RSS/Atom feeds. `INTERESTS` controls keyword scoring. `LOCATION` is included in the briefing context. `MAX_ITEMS` limits notifications.

## Deployment

Deploy the Python service to a worker platform such as Railway. Add the environment variables from `.env.example` as secrets. Schedule `python -m app.main --send-telegram` using the platform's cron/scheduled-job feature. Keep the service in read-only/draft mode until output has been reviewed for at least a week.

## Planned next steps

- Add source-specific adapters for job boards and official release feeds.
- Add SQLite/Postgres deduplication.
- Add an optional model step for explanations, with citations preserved.
- Add Telegram commands such as `/jobs`, `/ideas`, `/save`, and `/ignore`.
- Add human approval before drafting applications or contacting anyone.

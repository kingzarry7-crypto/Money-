# Opportunity Discovery Agent

This project has two separate modes:

- Scheduled briefing worker: `python -m app.main --send-telegram`
- Interactive Telegram command service: `python -m app.command_main`

The agent collects configured RSS/Atom feeds, ranks entries transparently, and sends research briefings. It does not apply for jobs, spend money, trade, publish content, or claim that an opportunity will make money.

## Telegram command service

Set these Railway variables:

```text
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
FEED_URLS=https://hnrss.org/newest,https://github.blog/feed/
LOCATION=London, UK
INTERESTS=AI automation,finance technology,software,remote work
MAX_ITEMS=5
```

For an always-on Railway service, set the start command to:

```bash
python -m app.command_main
```

Open your bot in Telegram, press Start, and use `/help`. Supported commands:

- `/start`
- `/help`
- `/briefing`
- `/jobs`
- `/ideas`
- `/releases`

The handler uses Telegram long polling, so it does not need a public webhook URL. Only the configured `TELEGRAM_CHAT_ID` receives replies when that variable is set. Keep the bot token in Railway variables, never in GitHub.

## Scheduled worker

For a Railway cron service, use:

```bash
python -m app.main --send-telegram
```

The cron worker runs once and exits. The interactive command service is a separate long-running service and should not use `restartPolicyType = "NEVER"`.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.command_main
```

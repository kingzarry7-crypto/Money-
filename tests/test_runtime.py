import pytest
from app import main


def test_telegram_mode_requires_credentials(monkeypatch):
    monkeypatch.setattr(main, "settings", lambda: type("Settings", (), {
        "feed_urls": [], "interests": [], "location": "London, UK", "max_items": 5,
        "telegram_bot_token": None, "telegram_chat_id": None,
    })())
    with pytest.raises(RuntimeError, match="TELEGRAM_BOT_TOKEN"):
        main.run(send_telegram=True)

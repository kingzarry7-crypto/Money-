from app.telegram_bot import allowed, response_for


def test_chat_filter():
    assert allowed(123, "123")
    assert not allowed(456, "123")


def test_unknown_command_is_safe():
    assert "do not recognise" in response_for("/unknown", "London, UK", [], [], 5)

from unittest.mock import patch

from email_utils import send_email


def test_send_email(monkeypatch):
    monkeypatch.setenv("SMTP_SERVER", "smtp.example.com")
    monkeypatch.setenv("SMTP_PORT", "587")
    monkeypatch.setenv("SMTP_USERNAME", "user@example.com")
    monkeypatch.setenv("SMTP_PASSWORD", "password")

    with patch("smtplib.SMTP") as mock_smtp:
        send_email("recipient@example.com", subject="Hi", body="Hello")

        mock_smtp.assert_called_with("smtp.example.com", 587)
        server = mock_smtp.return_value.__enter__.return_value
        server.starttls.assert_called_once()
        server.login.assert_called_once_with("user@example.com", "password")
        server.send_message.assert_called_once()

import os
import smtplib
from email.message import EmailMessage


def send_email(
    recipient: str,
    *,
    subject: str = "Script executed",
    body: str = "The script has been executed.",
) -> None:
    """Send a notification email using environment-provided SMTP settings."""

    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ.get("SMTP_PORT", 587))
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]

    message = EmailMessage()
    message["From"] = username
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)

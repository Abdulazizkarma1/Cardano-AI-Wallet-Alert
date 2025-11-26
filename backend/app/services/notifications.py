"""
Mock notification dispatcher service
This simulates sending notifications through various channels.
"""

from typing import Literal
from app.models.rule import Rule


def send_notification(channel: Literal["email", "sms", "push", "webhook"], message: str):
    """
    Mock function that simulates sending notifications.
    
    In production, this would integrate with:
    - Email: SendGrid, AWS SES, SMTP
    - SMS: Twilio, AWS SNS
    - Push: Firebase Cloud Messaging, OneSignal
    - Webhook: HTTP POST to configured URL
    
    Args:
        channel: Notification channel type
        message: Message content to send
    """
    print(f"[{channel.upper()}] {message}")


def notify_rule_triggered(rule: Rule, event_details: dict):
    """
    Send notification when a rule condition is met.
    
    Args:
        rule: Rule that was triggered
        event_details: Details about the detected event
    """
    message = (
        f"Alert: Wallet {rule.wallet_address[:20]}... "
        f"Condition '{rule.condition}' has been met. "
        f"Event: {event_details.get('details', {}).get('amount', 'N/A')}"
    )
    
    send_notification(rule.notification_channel, message)



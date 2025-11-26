"""
Mock blockchain event listener service
This simulates monitoring Cardano blockchain for wallet events.
"""

import random
from typing import Dict
from app.models.rule import Rule


def check_wallet_events(rule: Rule) -> Dict:
    """
    Mock function that simulates checking for blockchain events.
    
    In production, this would:
    - Connect to Cardano node or API (e.g., Blockfrost, Koios)
    - Query transaction history for the wallet
    - Evaluate conditions against recent transactions
    - Return event details if condition is met
    
    Args:
        rule: Rule object containing wallet address and condition
        
    Returns:
        Dictionary with event detection status and details
    """
    # Mock event detection - randomly returns events for demonstration
    event_detected = random.choice([True, False, False, False])  # 25% chance
    
    if event_detected:
        return {
            "event_detected": True,
            "wallet": rule.wallet_address,
            "condition_met": rule.condition,
            "timestamp": "2024-01-15T10:30:00Z",
            "details": {
                "transaction_hash": "abc123...",
                "amount": "150 ADA",
                "type": "receive"
            }
        }
    
    return {
        "event_detected": False,
        "wallet": rule.wallet_address,
        "last_checked": "2024-01-15T10:30:00Z"
    }


def start_listening(rule: Rule, callback):
    """
    Mock function to start continuous monitoring of a wallet.
    
    In production, this would:
    - Set up a polling loop or WebSocket connection
    - Periodically check wallet state
    - Call callback function when event is detected
    
    Args:
        rule: Rule to monitor
        callback: Function to call when event is detected
    """
    # Mock implementation - just logs
    print(f"[LISTENER] Started monitoring wallet: {rule.wallet_address}")
    print(f"[LISTENER] Condition: {rule.condition}")
    # In real implementation, this would run in background thread/process



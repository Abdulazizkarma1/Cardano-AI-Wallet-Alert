"""
Mock natural-language → rule parser service
This is a placeholder implementation that demonstrates the parsing structure.
"""

import re
from typing import Dict


def parse_instruction(text: str) -> Dict:
    """
    Mock parser that converts natural language into JSON rule structure.
    
    In production, this would use an LLM or NLP model to extract:
    - Wallet address
    - Condition (amount, type, etc.)
    - Timeframe
    - Notification preferences
    
    Args:
        text: Natural language instruction
        
    Returns:
        Dictionary with instruction and parsed_rule structure
    """
    # Mock extraction logic (simplified pattern matching)
    text_lower = text.lower()
    
    # Extract wallet address (mock pattern)
    wallet_match = re.search(r'addr[_\w]*[\w]{20,}', text)
    wallet = wallet_match.group(0) if wallet_match else "addr_test1..."
    
    # Extract amount and condition
    amount_match = re.search(r'(\d+(?:\.\d+)?)\s*ada', text_lower)
    amount = amount_match.group(1) if amount_match else "100"
    
    # Determine condition type
    if 'receive' in text_lower or 'incoming' in text_lower:
        condition = f"receive > {amount} ADA"
    elif 'send' in text_lower or 'outgoing' in text_lower:
        condition = f"send > {amount} ADA"
    else:
        condition = f"receive > {amount} ADA"  # default
    
    # Extract timeframe
    timeframe_match = re.search(r'(\d+)\s*(h|hour|hours|d|day|days)', text_lower)
    if timeframe_match:
        timeframe = f"{timeframe_match.group(1)}{timeframe_match.group(2)[0]}"
    else:
        timeframe = "1h"  # default
    
    return {
        "instruction": text,
        "parsed_rule": {
            "wallet": wallet,
            "condition": condition,
            "timeframe": timeframe
        }
    }



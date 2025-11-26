from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class Rule(BaseModel):
    """Rule model for wallet alert conditions"""
    id: Optional[str] = None
    wallet_address: str
    condition: str  # e.g., "receive > 100 ADA"
    timeframe: Optional[str] = None  # e.g., "1h", "24h"
    notification_channel: Literal["email", "sms", "push", "webhook"] = "email"
    created_at: Optional[datetime] = None
    active: bool = True


class RuleCreate(BaseModel):
    """Schema for creating a new rule"""
    wallet_address: str
    condition: str
    timeframe: Optional[str] = None
    notification_channel: Literal["email", "sms", "push", "webhook"] = "email"


class ParseRequest(BaseModel):
    """Schema for parsing natural language instruction"""
    instruction: str


class ParseResponse(BaseModel):
    """Schema for parsed rule response"""
    instruction: str
    parsed_rule: dict



"""
API routes for rule management
"""

from fastapi import APIRouter, HTTPException
from typing import List
from app.models.rule import Rule, RuleCreate
from app.services.parser import parse_instruction
from app.services.listener import check_wallet_events
from app.services.notifications import notify_rule_triggered
from datetime import datetime
import uuid

router = APIRouter(prefix="/rules", tags=["rules"])

# In-memory storage for demo purposes (use database in production)
rules_store: List[Rule] = []


@router.post("", response_model=Rule, status_code=201)
async def create_rule(rule_data: RuleCreate):
    """
    Create a new alert rule.
    
    Args:
        rule_data: Rule creation data
        
    Returns:
        Created rule object
    """
    new_rule = Rule(
        id=str(uuid.uuid4()),
        wallet_address=rule_data.wallet_address,
        condition=rule_data.condition,
        timeframe=rule_data.timeframe,
        notification_channel=rule_data.notification_channel,
        created_at=datetime.now(),
        active=True
    )
    
    rules_store.append(new_rule)
    
    # Mock: Start monitoring (in production, this would start background task)
    check_wallet_events(new_rule)
    
    return new_rule


@router.get("", response_model=List[Rule])
async def list_rules():
    """
    List all alert rules.
    
    Returns:
        List of all rules
    """
    return rules_store


@router.get("/{rule_id}", response_model=Rule)
async def get_rule(rule_id: str):
    """
    Get a specific rule by ID.
    
    Args:
        rule_id: Rule identifier
        
    Returns:
        Rule object
    """
    rule = next((r for r in rules_store if r.id == rule_id), None)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule


@router.delete("/{rule_id}", status_code=204)
async def delete_rule(rule_id: str):
    """
    Delete a rule by ID.
    
    Args:
        rule_id: Rule identifier
    """
    global rules_store
    rules_store = [r for r in rules_store if r.id != rule_id]
    return None



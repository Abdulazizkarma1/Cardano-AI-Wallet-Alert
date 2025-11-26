"""
API routes for natural language parsing
"""

from fastapi import APIRouter
from app.models.rule import ParseRequest, ParseResponse
from app.services.parser import parse_instruction

router = APIRouter(prefix="/parse", tags=["parse"])


@router.post("", response_model=ParseResponse)
async def parse_natural_language(request: ParseRequest):
    """
    Convert natural language instruction into structured rule format.
    
    Example input:
        "Alert me when wallet addr_test1... receives more than 100 ADA in the next hour"
    
    Args:
        request: ParseRequest containing natural language instruction
        
    Returns:
        ParseResponse with parsed rule structure
    """
    result = parse_instruction(request.instruction)
    return ParseResponse(**result)



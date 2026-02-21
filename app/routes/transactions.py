from fastapi import APIRouter, Depends
from typing import List
from app.models.transactions import Transaction, Expense
from app.services.transactions import build_transactions
from app.utils.security import validate_api_key



router = APIRouter(perfix="/blackrock/challenge/v1", tags=["transactions"])



#==========================================
# Transaction Builder
#==========================================

@router.post("/transactions:parse", response_model=List[Transaction])
async def parse_transactions(expenses: List[Expense], auth: str = Depends(validate_api_key)):
    """
    Endpoint: Transaction Builder
    Input: List of expenses
    Output: List of transactions with ceiling and remanent
    """
    return build_transactions(expenses)
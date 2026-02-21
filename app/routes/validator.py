from fastapi import APIRouter, Depends
from app.models.transactions import TransactionValidatorResponse, TransactionValidatorRequest
from app.services.transactions import validate_transactions
from app.utils.security import validate_api_key



router = APIRouter(prefix="/blackrock/challenge/v1", tags=["validator"])



#==========================================
# Transaction Validator
#==========================================

@router.post("/transactions:filter", response_model=TransactionValidatorResponse)
async def validator(request: TransactionValidatorRequest, auth: str = Depends(validate_api_key)):
    """
    Endpoint: Transaction Validator
    Input: wage + transactions
    Output: valid vs invalid transactions
    """
    return validate_transactions(request)

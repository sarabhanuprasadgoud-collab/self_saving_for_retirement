from fastapi import APIRouter, Depends
from app.models.periods import TemporalConstraintResponse, TemporalConstraintRequest
from app.services.temporal import apply_temporal_constraints
from app.utils.security import validate_api_key



router = APIRouter(prefix="/blackrock/challenge/v1", tags=["temporal"])



#==========================================
# Temporal Constraints
#==========================================

@router.post("/transactions:filter", response_model=TemporalConstraintResponse)
async def filter_transactions(request: TemporalConstraintRequest, auth: str = Depends(validate_api_key)):
    """
    Endpoint: Temporal Constraints Validator
    Input: q, p, k periods + transactions
    Output: valid vs invalid transactions with adjustments
    """
    return apply_temporal_constraints(request)
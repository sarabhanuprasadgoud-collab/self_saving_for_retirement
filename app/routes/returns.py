from fastapi import APIRouter, Depends
from app.models.returns import ReturnsResponse, ReturnsRequest
from app.services.returns import calculate_returns
from app.utils.security import validate_api_key



router = APIRouter(prefix="/blackrock/challenge/v1", tags=["returns"])



#==========================================
# Returns Calculation for NPS
#==========================================

@router.post("/returns:nps", response_class=ReturnsResponse)
async def returns_nps(request: ReturnsRequest, auth: str = Depends(validate_api_key)):
    """
    Endpoint: NPS Returns Calculation
    """
    return calculate_returns(request, request.transactions, instrument="nps")



#==========================================
# Returns Calculation for Index
#==========================================

@router.post("/returns:index", response_class=ReturnsResponse)
async def returns_nps(request: ReturnsRequest, auth: str = Depends(validate_api_key)):
    """
    Endpoint: Index Fund Returns Calculation
    """
    return calculate_returns(request, request.transactions, instrument="index")
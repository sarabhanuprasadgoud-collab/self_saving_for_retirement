from fastapi import APIRouter, Depends
from app.models.performance import PerformanceReport
from app.services.performance import generate_performance_report
from app.utils.security import validate_api_key



router = APIRouter(prefix="/blackrock/challenge/v1", tags=["performance"])



#==========================================
# Performance Report
#==========================================

@router.post("/performance", response_model=PerformanceReport)
async def performance(auth: str = Depends(validate_api_key)):
    """
    Endpoint: Performance Report
    Output: system metrics (time, memory, threads)
    """
    return generate_performance_report()
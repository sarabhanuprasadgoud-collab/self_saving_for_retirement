from pydantic import BaseModel, Field
from datetime import datetime
from app.models.transactions import Expense, Transaction, InvalidTransaction
from typing import List


#==========================================
# Period Models 
#==========================================

class QPeriod(BaseModel):
    fixed: float = Field(..., ge=0, le=5e5)
    start: datetime
    end: datetime

class PPeriod(BaseModel):
    extra: float = Field(..., ge=0, le=5e5)
    start: datetime
    end: datetime

class KPeriod(BaseModel):
    start: datetime
    end: datetime


#==========================================
# Temporal Constraints Models 
#==========================================

class TemporalConstraintRequest(BaseModel):
    q: List[QPeriod] = []
    p: List[PPeriod] = []
    k: List[KPeriod] = []
    wage: float = Field(..., gt=0)
    transactions: List[Expense]

class TemporalValidTransaction(Transaction):
    inKPeriod: bool = False

class TemporalConstraintResponse(BaseModel):
    valid: List[TemporalValidTransaction]
    invalid: List[InvalidTransaction]
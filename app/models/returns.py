from pydantic import BaseModel, Field
from datetime import datetime
from app.models.periods import QPeriod, PPeriod, KPeriod
from app.models.transactions import Transaction
from typing import List

#==========================================
# Returns Models 
#==========================================

class ReturnsRequest(BaseModel):
    age: int = Field(..., ge=0)
    wage: float = Field(..., gt=0)
    inflation: float = Field(..., ge=0)
    q: List[QPeriod] = []
    p: List[PPeriod] = []
    k: List[KPeriod] = []
    transactions: List[Transaction]

class SavingsByDate(BaseModel):
    start: datetime
    end: datetime
    amount: float
    profit: float | None = None # For NPS
    taxBenifit: float | None = None # For NPS
    returnValue: float | None = None # For Index

class ReturnsResponse(BaseModel):
    totalTransactionAmount: float
    totalCeiling: float
    savingsByDates: List[SavingsByDate]
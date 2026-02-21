from pydantic import BaseModel, Field, RootModel
from datetime import datetime
from typing import List


#==========================================
# Transaction Builder Models 
#==========================================

class Expense(BaseModel):
    date: datetime
    amount: float = Field(..., ge=0, le=5e5)

class Transaction(BaseModel):
    date: datetime
    amount: float
    ceiling: float
    remanent: float

class TransactionList(RootModel[List[Expense]]):
    """
    Root model wrapper for a list of Expense objects.
    Required in Pydantic v2 instead of __root__.
    """
    pass

#==========================================
# Transaction Validator Models 
#==========================================
class TransactionValidatorRequest(BaseModel):
    wage: float = Field(..., gt=0)
    transactions: List[Transaction]

class InvalidTransaction(Transaction):
    message: str

class TransactionValidatorResponse(BaseModel):
    valid: List[Transaction]
    invalid: List[Transaction]
from typing import List, Tuple
from app.models.transactions import Expense, Transaction, InvalidTransaction, TransactionValidatorRequest, TransactionValidatorResponse


#==========================================
# Transaction Builder Service
#==========================================

def build_transactions(expenses: List[Expense]) -> List[Transaction]:
    """
    Service function to enrich raw expenses with ceiling and remanent.
    Return list of transactions
    """

    transactions = []

    for exp in expenses:

        # Ceiling: round up to next multiple of 100
        ceiling = ((exp.amount + 99) // 100) * 100

        # Remanent: difference between ceiling and original amount
        remanent = ceiling - exp.amount

        # Edge case: if amount is already multiple of 100 -> remanent = 0
        if exp.amount % 100 == 0:
            remanent = 0
        
        transactions.append(
            Transaction(
                date=exp.date,
                amount=exp.amount,
                ceiling=ceiling,
                remanent=remanent
            )
        )
    return transactions


#==========================================
# Transaction Builder Service
#==========================================

def validate_transactions(request: TransactionValidatorRequest) -> TransactionValidatorResponse:
    """
    Service function to validate transactions.
    Return valid vs invalid transactions.
    Rules:
      - Check for negative amounts, as negative amounts are invalid.
      - Check duplicates (same date), as duplicate dates are invalid.
      - Wage must be positive (already enforced by Pydantic).
    """
    valid, invalid = [], []
    seen_dates = set()

    for txn in request.transactions:

        # Rule 1: Negative amounts
        if txn.amount < 0:
            invalid.append(InvalidTransaction(**txn.model_dump(), message="Negative amounts are not allowed"))
            continue

        # Rule 2: Duplicate dates
        if txn.date in seen_dates:
            invalid.append(InvalidTransaction(**txn.model_dump(), message="Duplicate transaction"))

        # If valid, add to list
        valid.append(txn)
        seen_dates.add(txn.date)

    return TransactionValidatorResponse(valid=valid, invalid=invalid)
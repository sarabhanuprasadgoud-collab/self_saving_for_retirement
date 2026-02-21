# ====================================================
# Test type: Unit Test
# Validation: Negative amounts and duplicates
# Command: pytest tests/test_validator.py
# ====================================================

import pytest
from datetime import datetime
from app.models.transactions import Transaction, TransactionValidatorRequest
from app.services.transactions import validate_transactions

def test_validate_transactions_negative_amount():
    tx = Transaction(date=datetime(2023,7,10,9,15,0), amount=-250, ceiling=200, remanent=30)
    request = TransactionValidatorRequest(wage=50000, transactions=[tx])
    response = validate_transactions(request)
    assert len(response.invalid) == 1
    assert response.invalid[0].message == "Negative amounts are not allowed"

def test_validate_transactions_duplicate():
    tx1 = Transaction(date=datetime(2023,1,15,10,30,0), amount=2000, ceiling=300, remanent=50)
    tx2 = Transaction(date=datetime(2023,1,15,10,30,0), amount=3000, ceiling=400, remanent=100)
    request = TransactionValidatorRequest(wage=50000, transactions=[tx1, tx2])
    response = validate_transactions(request)
    assert len(response.invalid) == 1
    assert response.invalid[0].message == "Duplicate transaction"
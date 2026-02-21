# ====================================================
# Test type: Unit Test
# Validation: Ceiling and remanent calculation
# Command: pytest tests/test_transactions.py
# ====================================================

import pytest
from datetime import datetime
from app.models.transactions import Expense, Transaction
from app.services.transactions import build_transactions

def test_build_transactions_basic():
    expenses = [Expense(date=datetime(2023,10,12,20,15,30), amount=250)]
    txs = build_transactions(expenses)
    assert txs[0].ceiling == 300
    assert txs[0].remanent == 50

def test_build_transactions_multiple_of_100():
    expenses = [Expense(date=datetime(2023,10,12,20,15,30), amount=500)]
    txs = build_transactions(expenses)
    assert txs[0].ceiling == 500
    assert txs[0].remanent == 0
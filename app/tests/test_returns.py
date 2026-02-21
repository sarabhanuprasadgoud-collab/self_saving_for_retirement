# ====================================================
# Test type: Unit Test
# Validation: Compound interest, inflation adjustment, NPS tax benefit
# Command: pytest tests/test_returns.py
# ====================================================

import pytest
from datetime import datetime
from app.models.transactions import Transaction
from app.models.periods import KPeriod
from app.models.returns import ReturnsRequest
from app.services.returns import calculate_returns

def test_returns_nps():
    txs = [Transaction(date=datetime(2023,2,28,15,49,20), amount=375, ceiling=400, remanent=25)]
    k = [KPeriod(start=datetime(2023,1,1,0,0,0), end=datetime(2023,12,31,23,59,59))]
    request = ReturnsRequest(age=29, wage=50000, inflation=5.5, q=[], p=[], k=k, transactions=txs)

    response = calculate_returns(request, txs, instrument="nps")
    assert response.savingsByDates[0].taxBenifit >= 0
    assert response.savingsByDates[0].profit is not None

def test_returns_index():
    txs = [Transaction(date=datetime(2023,2,28,15,49,20), amount=375, ceiling=400, remanent=25)]
    k = [KPeriod(start=datetime(2023,1,1,0,0,0), end=datetime(2023,12,31,23,59,59))]
    request = ReturnsRequest(age=29, wage=50000, inflation=5.5, q=[], p=[], k=k, transactions=txs)

    response = calculate_returns(request, txs, instrument="index")
    assert response.savingsByDates[0].returnValue is not None
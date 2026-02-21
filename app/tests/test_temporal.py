# ====================================================
# Test type: Unit Test
# Validation: q fixed override, p extra addition, k grouping
# Command: pytest tests/test_temporal.py
# ====================================================

import pytest
from datetime import datetime
from app.models.transactions import Expense
from app.models.periods import QPeriod, PPeriod, KPeriod, TemporalConstraintRequest
from app.services.temporal import apply_temporal_constraints

def test_temporal_constraints_q_and_p():
    expenses = [Expense(date=datetime(2023,10,12,20,15,30), amount=250)]
    q = [QPeriod(fixed=0, start=datetime(2023,10,1,0,0,0), end=datetime(2023,10,31,23,59,59))]
    p = [PPeriod(extra=25, start=datetime(2023,10,1,0,0,0), end=datetime(2023,12,31,23,59,59))]
    k = [KPeriod(start=datetime(2023,1,1,0,0,0), end=datetime(2023,12,31,23,59,59))]

    request = TemporalConstraintRequest(q=q, p=p, k=k, wage=50000, transactions=expenses)
    response = apply_temporal_constraints(request)

    assert response.valid[0].remanent == 25  # q fixed=0, then p adds 25
    assert response.valid[0].inKPeriod is True
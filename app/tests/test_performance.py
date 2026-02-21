# ====================================================
# Test type: Unit Test
# Validation: System metrics reporting
# Command: pytest tests/test_performance.py
# ====================================================

import pytest
from app.services.performance import generate_performance_report

def test_performance_report():
    report = generate_performance_report()
    assert "MB" in report.memory
    assert isinstance(report.threads, int)
    assert isinstance(report.time, str)
from typing import List
from app.models.returns import ReturnsRequest, ReturnsResponse, SavingsByDate
from app.models.transactions import Transaction
from app.models.periods import KPeriod
import math


#==========================================
# Returns Calculation Service 
#==========================================

#------------------------------------------
# Tax Calculation
#------------------------------------------

def calculate_tax(income: float) -> float:
    """
    Simplified tax calculation based on slabs.
    """
    match income:
        case _ if income <= 700000:
            return 0
        case _ if income <= 1000000:
            return (income - 700000) * 0.10
        case _ if income <= 1200000:
            return (300000 * 0.10) + (income - 1000000) * 0.15
        case _ if income <= 1500000:
            return (300000 * 0.10) + (200000 * 0.15) + (income - 1200000) * 0.20
        case _:
            return (300000 * 0.10) + (200000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30
    


#------------------------------------------
# Compound Interest Calculation
#------------------------------------------

def compound_interest(principal: float, rate: float, years: int) -> float:
    """
    Compound interest formula: A = P * (1 + r)^t
    Annual compounding assumed (n=1).
    """
    return principal * math.pow((1 + rate), years)



#------------------------------------------
# Inflation Adjustment Calculation
#------------------------------------------

def inflation_adjustment(amount: float, inflation: float, years: int) -> float:
    """
    Inflation adjustment: A_real = A / (1 + inflation)^t
    """
    return amount / math.pow( (1 + (inflation / 100)), years)


#------------------------------------------
# NPS Returns Calculation
#------------------------------------------
def calculate_nps_returns(request: ReturnsRequest, k_period: KPeriod, period_amount: float, years: int) -> SavingsByDate:

    # NPS return
    final_value = compound_interest(period_amount, 0.0711, years)
    real_value = inflation_adjustment(final_value, request.inflation, years)

    # Tax benefit calculation
    annual_income = request.wage * 12
    nps_deduction = min(period_amount, 0.1 * annual_income, 200000)
    tax_benifit = calculate_tax(annual_income) - calculate_tax(annual_income - nps_deduction)

    return SavingsByDate(
        start=k_period.start,
        end=k_period.end,
        amount=period_amount,
        profit=real_value - period_amount,
        taxBenifit=tax_benifit
    )



#------------------------------------------
# Index Fund Returns Calculation
#------------------------------------------
def calculate_index_returns(request: ReturnsRequest, k_period: KPeriod, period_amount: float, years: int) -> SavingsByDate:

    # Index Fund return
    final_value = compound_interest(period_amount, 0.1449, years)
    real_value = inflation_adjustment(final_value, request.inflation, years)

    return SavingsByDate(
        start=k_period.start,
        end=k_period.end,
        amount=period_amount,
        returnValue=real_value
    )



#------------------------------------------
# Returns Calculation
#------------------------------------------


def calculate_returns(request: ReturnsRequest, transactions: List[Transaction], instrument: str) -> ReturnsResponse:
    """
    Service function to calculate returns for NPS or Index Fund.
    """
    total_amount = sum(txn.amount for txn in transactions)
    total_ceiling = sum(txn.ceiling for txn in transactions)

    savings_by_dates = []

    # Edge case: age ≥ 60 → use 5 years.
    years = (60 - request.age) if request.age < 60 else 5

    for k in request.k:

        # Filter transactions within k period
        period_txns = [txn for txn in transactions if k.start <= txn.date <= k.end]
        period_amount = sum(txn.remanent for txn in period_txns)
        savings = None
        if instrument == "nps":
            savings: SavingsByDate = calculate_nps_returns(request, k, period_amount, years)
        elif instrument == "index":
            savings: SavingsByDate = calculate_index_returns(request, k, period_amount, years)
        savings_by_dates.append(savings)

    return ReturnsResponse(
        totalTransactionAmount=total_amount,
        totalCeiling=total_ceiling,
        savingsByDates=savings_by_dates
    )
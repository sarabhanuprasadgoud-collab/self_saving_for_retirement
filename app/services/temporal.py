from app.models.periods import TemporalConstraintRequest, TemporalConstraintResponse, TemporalValidTransaction
from app.models.transactions import InvalidTransaction


#==========================================
# Temporal Constraints Service
#==========================================

def apply_temporal_constraints(request: TemporalConstraintRequest) -> TemporalConstraintResponse:
    """
    Service function to apply q, p, k rules.
    Rules:
      - q periods: override remanent with fixed amount (latest start wins).
      - p periods: add extra amounts (all applicable extras summed).
      - k periods: group transactions by date ranges.
    """

    valid, invalid = [], []
    seen_dates = set()

    for exp in request.transactions:

        # Reject negative amounts
        if exp.amount < 0:
            invalid.append(InvalidTransaction(
                date=exp.date,
                amount=exp.amount,
                ceiling=0,
                remanent=0,
                message="Negative amounts are not allowed"
            ))
            continue

        # Reject duplicates
        if exp.date in seen_dates:
            invalid.append(InvalidTransaction(
                date=exp.date,
                amount=exp.amount,
                ceiling=0,
                remanent=0,
                message="Duplicate transaction"
            ))
            continue

        seen_dates.add(exp.date)

        # Step 1: Calculate ceiling and remanent
        ceiling = ((exp.amount + 99) // 100) * 100
        remanent = ceiling - exp.amount
        if exp.amount % 100 == 0:
            remanent = 0

        # Step 2: Apply q rules (fixed override)
        applicable_q = [q for q in request.q if q.start <= exp.date <= q.end]
        if applicable_q:
            # Pick the one with latest start date
            chosen_q = max(applicable_q, key=lambda q: q.start)
            remanent = chosen_q.fixed

        # Step 3: Apply p rules (extra addition)
        applicable_p = [p for p in request.p if p.start <= exp.date <= p.end]
        if applicable_p:
            remanent += sum(p.extra for p in applicable_p)

        # Step 4: Mark if transaction falls in any k period
        in_k = any(k.start <= exp.date <= k.end for k in request.k)

        valid.append(TemporalValidTransaction(
            date=exp.date,
            amount=exp.amount,
            ceiling=ceiling,
            remanent=remanent,
            inKPeriod=in_k
        ))
        
    return TemporalConstraintResponse(valid=valid, invalid=invalid)
from fastapi import FastAPI
from app.routes import transactions, validator, temporal, returns, performance



#==========================================
# Main Application
#==========================================

app = FastAPI(title="BlackRock Hackathon API")



#==========================================
# Register routers
#==========================================
# Each route will:
# - Accept validated input (Pydantic models).
# - Call the corresponding service function.
# - Return structured JSON response.
app.include_router(transactions.router)
app.include_router(validator.router)
app.include_router(temporal.router)
app.include_router(returns.router)
app.include_router(performance.router)
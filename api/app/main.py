from fastapi import FastAPI, HTTPException

from app.fault_injection import (
    FaultType,
    inject_malformed_data,
    should_inject_fault
)

from app.generator import generate_market_data

app = FastAPI(
    title="Mock Market Data API",
    description="Simulates real-time financial market data",
    version="1.0.0"
)


@app.get("/")
async def root():

    return {"message": "API is working"}


@app.get("/v1/market-data")
async def get_market_data():

    fault_type = should_inject_fault()

    if fault_type == FaultType.INTERNAL_ERROR:

        raise HTTPException(
            status_code=500,
            detail="Injected internal server error"
        )

    if fault_type == FaultType.MALFORMED_DATA:

        return inject_malformed_data()

    return generate_market_data()
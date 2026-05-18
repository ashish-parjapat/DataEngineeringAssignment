from datetime import datetime

from pydantic import BaseModel


class MarketData(BaseModel):

    instrument_id: str
    price: float
    volume: float
    timestamp: datetime
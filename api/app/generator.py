import random
from datetime import datetime, timezone


INSTRUMENTS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "TSLA",
    "BTC-USD",
    "ETH-USD"
]


def generate_market_data():

    market_data = []

    for instrument in INSTRUMENTS:

        for _ in range(5):

            base_price = random.uniform(100, 50000)

            record = {
                "instrument_id": instrument,
                "price": round(base_price, 2),
                "volume": round(random.uniform(10, 10000), 2),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

            market_data.append(record)

    return market_data
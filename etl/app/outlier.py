from collections import defaultdict


def detect_outliers(records):

    instrument_prices = defaultdict(list)

    for record in records:

        instrument_prices[record.instrument_id].append(record.price)

    average_prices = {}

    for instrument_id, prices in instrument_prices.items():

        average_prices[instrument_id] = (
            sum(prices) / len(prices)
        )

    outliers = []

    for record in records:

        average_price = average_prices[record.instrument_id]

        deviation_percentage = abs(
            (record.price - average_price)
            / average_price
        ) * 100

        if deviation_percentage > 15:

            outliers.append(
                {
                    "instrument_id": record.instrument_id,
                    "price": record.price,
                    "average_price": round(average_price, 2),
                    "deviation_percentage": round(
                        deviation_percentage,
                        2
                    )
                }
            )

    return outliers
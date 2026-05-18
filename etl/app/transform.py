from collections import defaultdict


def calculate_vwap(records):

    instrument_data = defaultdict(
        lambda: {
            "total_price_volume": 0,
            "total_volume": 0
        }
    )

    for record in records:

        instrument_id = record.instrument_id

        instrument_data[instrument_id]["total_price_volume"] += (
            record.price * record.volume
        )

        instrument_data[instrument_id]["total_volume"] += (
            record.volume
        )

    vwap_result = {}

    for instrument_id, values in instrument_data.items():

        vwap = (
            values["total_price_volume"]
            / values["total_volume"]
        )

        vwap_result[instrument_id] = round(vwap, 2)

    return vwap_result
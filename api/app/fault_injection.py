import random
from enum import Enum

from app.generator import generate_market_data


class FaultType(Enum):
    NONE = "none"
    INTERNAL_ERROR = "internal_error"
    MALFORMED_DATA = "malformed_data"


def should_inject_fault():

    random_number = random.random()

    # 5% total fault chance
    if random_number < 0.025:
        return FaultType.INTERNAL_ERROR

    elif random_number < 0.05:
        return FaultType.MALFORMED_DATA

    return FaultType.NONE


def inject_malformed_data():

    data = generate_market_data()

    # corrupt one record intentionally
    data[0]["price"] = "INVALID_PRICE"

    return data
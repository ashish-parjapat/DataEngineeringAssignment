from pydantic import ValidationError

from app.schema import MarketData


def validate_market_data(data):

    valid_records = []

    invalid_records = []

    for record in data:

        try:

            validated_record = MarketData(**record)

            valid_records.append(validated_record)

        except ValidationError as error:

            invalid_records.append(
                {
                    "record": record,
                    "error": str(error)
                }
            )

    return valid_records, invalid_records
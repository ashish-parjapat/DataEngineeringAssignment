import time

from app.extract import extract_market_data
from app.load import load_market_data
from app.logger import logger
from app.outlier import detect_outliers
from app.transform import calculate_vwap
from app.validate import validate_market_data


def main():

    start_time = time.time()

    data = extract_market_data()

    if not data:

        logger.error("No data received")

        return

    valid_records, invalid_records = validate_market_data(data)

    logger.info(
        f"Records Processed: {len(valid_records)}"
    )

    logger.info(
        f"Records Dropped: {len(invalid_records)}"
    )

    vwap_result = calculate_vwap(valid_records)

    logger.info(f"VWAP: {vwap_result}")

    outliers = detect_outliers(valid_records)

    logger.info(f"Outliers Detected: {len(outliers)}")

    load_market_data(valid_records)

    end_time = time.time()

    execution_time = round(end_time - start_time, 2)

    logger.info(
        f"Execution Time: {execution_time} seconds"
    )


if __name__ == "__main__":

    main()
from app.extract import extract_market_data
from app.transform import calculate_vwap
from app.validate import validate_market_data
from app.outlier import detect_outliers


def main():

    data = extract_market_data()

    if not data:

        print("No data received")

        return

    valid_records, invalid_records = validate_market_data(data)

    print("\nVALID RECORDS:")
    print(valid_records)

    print("\nINVALID RECORDS:")
    print(invalid_records)

    vwap_result = calculate_vwap(valid_records)

    print("\nVWAP:")
    print(vwap_result)

    outliers = detect_outliers(valid_records)

    print("\nOUTLIERS:")
    print(outliers)

if __name__ == "__main__":

    main()
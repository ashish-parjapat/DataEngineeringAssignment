import requests

API_URL = "http://api:8000/v1/market-data"


def extract_market_data():

    try:

        response = requests.get(API_URL, timeout=5)

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.Timeout:

        print("Request timed out")

    except requests.exceptions.HTTPError as error:

        print(f"HTTP error occurred: {error}")

    except requests.exceptions.RequestException as error:

        print(f"Request failed: {error}")

    return None
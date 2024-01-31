import requests, json

# Streak BASE API
STREAK_SCANNER_DATA_BASE_URL = "https://api-op.streak.tech/open_screener/?slug="
STREAK_SCANNER_LIST_BASE_URL = "https://s-op.streak.tech/screeners/multi_search"

def get_scanner_data(scanner_slug):
    try:
        payload = {}
        headers = {}
        response = requests.get(f"{STREAK_SCANNER_DATA_BASE_URL}{scanner_slug}", headers=headers, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error in getting {scanner_slug} data : {e}")
        raise e

def get_all_scanners(page_size=100, page_number=1):
    try:
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({
                "page_size": page_size,
                "return_fields": [],
                "query_fields": [
                    "screener_logic",
                    "screener_name"
                ],
                "query": "",
                "page_number": page_number,
                "search": {
                    "sample": [
                        True
                    ],
                    "screener_uuid": [],
                    "time_frame": [
                        "day"
                    ],
                    "universe": [
                        "Nifty 500"
                    ],
                    "chart_type": [
                        "candlestick"
                    ]
                },
                "sort": {
                    "symbol_count": "desc"
                }
        })
        response = requests.post(f"{STREAK_SCANNER_LIST_BASE_URL}", headers=headers, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error in get_and_store_scanners : {e}")
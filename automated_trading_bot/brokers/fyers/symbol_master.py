import csv
import requests
from io import StringIO

def download_symbol_master(csv_url):
    response = requests.get(csv_url)
    if response.status_code == 200:
        csv_data = StringIO(response.text)
        csv_reader = csv.reader(csv_data)
        symbol_master_data = list(csv_reader)
        return symbol_master_data
    else:
        print("Failed to download symbol master data.")
        return []

# Example usage:
csv_url = 'https://public.fyers.in/sym_details/NSE_CM.csv'
symbol_master_data = download_symbol_master(csv_url)

def get_symbols_by_exchange(symbol_master_data, exchange_code):
    """
    Get symbols based on the exchange code.

    Parameters:
    - symbol_master_data (list): List of lists containing raw symbol master data.
    - exchange_code (int): Exchange code.

    Returns:
    - list: List of symbols for the given exchange code.
    """
    return [symbol[9] for symbol in symbol_master_data if symbol[8].isdigit() and int(symbol[8]) == exchange_code]

def get_symbols_by_segment(symbol_master_data, segment_code):
    """
    Get symbols based on the segment code.

    Parameters:
    - symbol_master_data (list): List of lists containing raw symbol master data.
    - segment_code (int): Segment code.

    Returns:
    - list: List of symbols for the given segment code.
    """
    return [symbol[9] for symbol in symbol_master_data if symbol[10].isdigit() and int(symbol[10]) == segment_code]


def get_symbol_details(symbol_master_data, symbol_ticker):
    """
    Get details for a specific symbol.

    Parameters:
    - symbol_master_data (list): List of lists containing raw symbol master data.
    - symbol_ticker (str): Symbol ticker.

    Returns:
    - list: List containing details for the given symbol ticker.
    """
    for symbol in symbol_master_data:
        if symbol[9] == symbol_ticker:
            return symbol

    return None

# Get symbols for NSE Equity Derivatives (exchange code: 10, segment code: 11)
nse_equity_derivative_symbols = get_symbols_by_exchange(symbol_master_data, exchange_code=10)
print("NSE Equity Derivative Symbols:", nse_equity_derivative_symbols)

# Get symbols for BSE Capital Market (exchange code: 12, segment code: 10)
bse_capital_market_symbols = get_symbols_by_exchange(symbol_master_data, exchange_code=12)
print("BSE Capital Market Symbols:", bse_capital_market_symbols)

# Get details for a specific symbol (e.g., 'NSE:ARE&M-EQ')
symbol_details = get_symbol_details(symbol_master_data, symbol_ticker='NSE:SBIN-EQ')
print("Symbol Details:", symbol_details)

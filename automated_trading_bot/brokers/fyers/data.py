from login import get_fyers_model


fyers = get_fyers_model()

def get_historical_data(symbol, resolution, range_from, range_to, cont_flag):
    """
    Get historical data using the Fyers API.

    Parameters:
    - symbol (str): Symbol for which historical data is requested (e.g., "NSE:SBIN-EQ").
    - resolution (str): Candle resolution (e.g., "D" for daily).
    - date_format (int): Date format flag (0 for epoch value, 1 for yyyy-mm-dd format).
    - range_from (str): Start date of records (accepts epoch value or yyyy-mm-dd format).
    - range_to (str): End date of records (accepts epoch value or yyyy-mm-dd format).
    - cont_flag (int): Continues data flag (1 for continuous data).

    Returns:
    - dict: Dictionary containing historical data.
    """

    # Prepare data for the API request
    data = {
        "symbol": symbol,
        "resolution": resolution,
        "date_format": 1,
        "range_from": str(range_from),
        "range_to": str(range_to),
        "cont_flag": cont_flag
    }

    # Make the API request
    response = fyers.history(data=data)

    # Return the response
    return response

sbi_data = get_historical_data("NSE:SBIN-EQ", "15", "2024-01-09", "2024-01-11", 0)
print(sbi_data)

def get_quotes(symbols):
    """
    Get market quotes for one or more symbols using the Fyers API.

    Parameters:
    - symbols (str): Comma-separated symbols for which quotes are requested (e.g., "NSE:SBIN-EQ,NSE:IDEA-EQ").

    Returns:
    - dict: Dictionary containing market quotes for the provided symbols.
    """
    # Prepare data for the API request
    data = {
        "symbols": symbols
    }

    # Make the API request
    response = fyers.quotes(data=data)

    # Return the response
    return response

# symbols = "NSE:SBIN-EQ"
# quotes_data = get_quotes(symbols)
# print(quotes_data)



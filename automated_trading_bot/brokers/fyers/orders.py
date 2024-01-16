import requests
from login import get_fyers_model


## Fyers model instance 
fyers = get_fyers_model()

def place_fyers_order(symbol, qty, order_type, side, product_type, limit_price=0, stop_price=0,
                      disclosed_qty=0, validity="DAY", offline_order=False, order_tag=None):
    """
    Place an order using the Fyers API.

    Parameters:
    - symbol (str): Symbol of the asset, e.g., "NSE:SBIN-EQ".
    - qty (int): Quantity of the asset.
    - order_type (int): Order type (1: Limit, 2: Market, 3: Stop, 4: Stop Limit).
    - side (int): Order side (1: Buy, -1: Sell).
    - product_type (str): Product type (CNC, INTRADAY, MARGIN, CO, BO).
    - limit_price (float): Limit price for Limit and Stop Limit orders.
    - stop_price (float): Stop price for Stop and Stop Limit orders.
    - disclosed_qty (int): Disclosed quantity (only for Equity).
    - validity (str): Order validity ("IOC" or "DAY").
    - offline_order (bool): Offline order flag.
    - order_tag (str): (Optional)Tag to assign to the specific order.

    Returns:
    - dict: Response from the Fyers API.
    """
    

    data = {
        "symbol": symbol,
        "qty": qty,
        "type": order_type,
        "side": side,
        "productType": product_type,
        "limitPrice": limit_price,
        "stopPrice": stop_price,
        "validity": validity,
        "disclosedQty": disclosed_qty,
        "offlineOrder": offline_order,
        "orderTag": order_tag
    }

    response = fyers.place_order(data=data)
    return response

def place_fyers_basket_orders(orders):
    """
    Place multiple orders simultaneously using the Fyers API.

    Parameters:
    - orders (list): List of order dictionaries.

    Returns:
    - dict: Response from the Fyers API.
    """
    
    response = fyers.place_basket_orders(data=orders)
    return response

# orders = [
#     {
#         "symbol": "NSE:SBIN-EQ",
#         "qty": 1,
#         "type": 2,
#         "side": 1,
#         "productType": "INTRADAY",
#         "limitPrice": 0,
#         "stopPrice": 0,
#         "validity": "DAY",
#         "disclosedQty": 0,
#         "offlineOrder": False,
#     },
#     {
#         "symbol": "NSE:IDEA-EQ",
#         "qty": 1,
#         "type": 2,
#         "side": 1,
#         "productType": "INTRADAY",
#         "limitPrice": 0,
#         "stopPrice": 0,
#         "validity": "DAY",
#         "disclosedQty": 0,
#         "offlineOrder": False,
#     },
#     {
#         "symbol": "NSE:SBIN-EQ",
#         "qty": 1,
#         "type": 2,
#         "side": 1,
#         "productType": "INTRADAY",
#         "limitPrice": 0,
#         "stopPrice": 0,
#         "validity": "DAY",
#         "disclosedQty": 0,
#         "offlineOrder": False,
#     },
#     {
#         "symbol": "NSE:IDEA-EQ",
#         "qty": 1,
#         "type": 2,
#         "side": 1,
#         "productType": "INTRADAY",
#         "limitPrice": 0,
#         "stopPrice": 0,
#         "validity": "DAY",
#         "disclosedQty": 0,
#         "offlineOrder": False,
#     }
# ]

def modify_fyers_order(order_id, order_type=None, limit_price=None, stop_price=None, qty=None):
    """
    Modify a pending order using the Fyers API.

    Parameters:
    - order_id (str): Order ID to be modified.
    - order_type (int): Order type (1: Limit, 2: Market, 3: Stop, 4: Stop Limit).
    - limit_price (float): Limit price for Limit and Stop Limit orders.
    - stop_price (float): Stop price for Stop and Stop Limit orders.
    - qty (int): Quantity of the asset.

    Returns:
    - dict: Response from the Fyers API.
    """
    

    data = {
        "id": order_id,
        "type": order_type,
        "limitPrice": limit_price,
        "stopPrice": stop_price,
        "qty": qty
    }

    response = fyers.modify_order(data=data)
    return response

# modified_data = {
#     "order_id": order_id,
#     "order_type": 1,  # Specify the new order type (if applicable)
#     "limit_price": 61049,  # Specify the new limit price (if applicable)
#     "qty": 1  # Specify the new quantity (if applicable)
# }

def modify_fyers_multi_orders(orders):
    """
    Modify multiple pending orders simultaneously using the Fyers API.

    Parameters:
    - orders (list): List of order modification dictionaries. Each dictionary should contain
                    the parameters for modifying a single order.

    Returns:
    - dict: Response from the Fyers API.
    """
    response = fyers.modify_basket_orders(data=orders)
    return response

# orders = [{
#     "id":orderId,
#     "type":1,
#     "limitPrice": 61049,
#     "qty":1
#   },
#   {
#     "id":orderId,
#     "type":1,
#     "limitPrice": 61049,
#     "qty":1 
#   }]
def cancel_fyers_order(order_id):
    """
    Cancel a pending order using the Fyers API.

    Parameters:
    - order_id (str): Order ID to be canceled.

    Returns:
    - dict: Response from the Fyers API.
    """

    data = {
        "id": order_id
    }

    response = fyers.cancel_order(data=data)
    return response

def cancel_multi_fyers_orders(order_ids):
    """
    Cancel multiple pending orders using the Fyers API.

    Parameters:
    - order_ids (list): List of order IDs to be canceled.

    Returns:
    - dict: Response from the Fyers API.
    """

    data = [{"id": order_id} for order_id in order_ids]

    response = fyers.cancel_basket_orders(data=data)
    return response

# order_ids_to_cancel = ['808058117761', '808058117762']

def exit_fyers_positions(position_ids=None):
    """
    Exit positions using the Fyers API.

    Parameters:
    - position_ids (list): List of position IDs to be closed. If not provided, all open positions will be closed.

    Returns:
    - dict: Response from the Fyers API.
    """

    data = {"id": position_ids} if position_ids else {}

    response = fyers.exit_positions(data=data)
    return response
# position_ids_to_exit = ['positionId1', 'positionId2']

def exit_fyers_positions_by_id(position_ids=None):
    """
    Exit positions by ID using the Fyers API.

    Parameters:
    - position_ids (str or list): Position ID or list of Position IDs to be closed.

    Returns:
    - dict: Response from the Fyers API.
    """

    data = {"id": position_ids} if position_ids else {}

    response = fyers.exit_positions(data=data)
    return response
# position_id_to_exit = "NSE:SBIN-EQ-BO"  # or a list of position IDs like ["NSE:SBIN-EQ-INTRADAY", "NSE:SBIN-EQ-CNC"]

def exit_fyers_positions_by_segment(segment, side, product_type):
    """
    Exit positions by segment, side, and productType using the Fyers API.

    Parameters:
    - segment (int): Segment value (e.g., 10 for Capital Market).
    - side (int): Side value (1 for Buy side, -1 for Sell side).
    - product_type (str): Product type (e.g., "INTRADAY", "CNC", "CO", "BO", "MARGIN", "ALL").

    Returns:
    - dict: Response from the Fyers API.
    """

    data = {
        "segment": segment,
        "side": side,
        "productType": product_type
    }

    response = fyers.exit_positions(data=data)
    return response

# segment_value = 10
# side_value = 1
# product_type_value = "MARGIN"

def cancel_pending_orders_fyers(access_token, position_id=None):
    """
    Cancel pending orders using the Fyers API.

    Parameters:
    - access_token (str): Fyers access token.
    - position_id (str, optional): Position ID for a specific symbol. Default is None.

    Returns:
    - dict: Response from the Fyers API.
    """
    url = "https://api-t1.fyers.in/api/v3/positions"
    
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}"
    }

    # Build the request body
    request_body = {"pending_orders_cancel": 1}
    if position_id:
        request_body["id"] = position_id

    # Send the DELETE request
    response = requests.delete(url, headers=headers, json=request_body)

    # Return the response as a dictionary
    return response.json()

def convert_position_fyers(access_token, symbol, overnight, position_side, convert_qty, convert_from, convert_to):
    """
    Convert an open position from one product type to another using the Fyers API.

    Parameters:
    - access_token (str): Fyers access token.
    - symbol (str): Position ID (symbol) to be converted (e.g., "MCX:SILVERMIC20NOVFUT").
    - overnight (int): Flag indicating if the position is carry forward (1) or taken today (0).
    - position_side (int): 1 for open long positions, -1 for open short positions.
    - convert_qty (int): Quantity to be converted (in multiples of lot size for derivatives).
    - convert_from (str): Existing product type (e.g., "INTRADAY").
    - convert_to (str): New product type (e.g., "CNC").

    Returns:
    - dict: Response from the Fyers API.
    """
    url = "https://api-t1.fyers.in/api/v3/positions"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}"
    }

    # Build the request body
    request_body = {
        "symbol": symbol,
        "overnight": overnight,
        "positionSide": position_side,
        "convertQty": convert_qty,
        "convertFrom": convert_from,
        "convertTo": convert_to
    }

    # Send the request
    response = requests.post(url, headers=headers, json=request_body)

    # Return the response as a dictionary
    return response.json()

# data = {
#     "symbol": "MCX:SILVERMIC20NOVFUT",
#     "overnight": 0,
#     "positionSide": 1,
#     "convertQty": 1,
#     "convertFrom": "INTRADAY",
#     "convertTo": "CNC"
# }
# convert_position_fyers(access_token, **data)


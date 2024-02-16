from fyers_apiv3.FyersWebsocket import data_ws

def data_ws_connection(app_id_access_token, onopen, onclose, onerror, onmessage):
    fyers = data_ws.FyersDataSocket(
        access_token=app_id_access_token,       # Access token in the format "appid:accesstoken"
        log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
        litemode=True,                  # Lite mode disabled. Set to True if you want a lite response.
        write_to_file=False,              # Save response in a log file instead of printing it.
        reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
        on_connect=onopen,               # Callback function to subscribe to data upon connection.
        on_close=onclose,                # Callback function to handle WebSocket connection close events.
        on_error=onerror,                # Callback function to handle WebSocket errors.
        on_message=onmessage,            # Callback function to handle incoming messages from the WebSocket.
        reconnect_retry=10               # Number of times reconnection will be attepmted in case
    )
    return fyers



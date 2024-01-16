from decouple import config


fyers_client_id=config('fyers_client_id', default='')
fyers_secret_id=config('fyers_secret_id', default='')
fyers_redirect_uri=config('fyers_redirect_uri', default='')
fyers_id=config('fyers_id', default='')
fyers_pin=config('fyers_pin', default='')
fyers_TOTP_KEY=config('fyers_TOTP_KEY', default='')

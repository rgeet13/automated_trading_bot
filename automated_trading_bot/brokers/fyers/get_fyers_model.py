import os
from fyers_apiv3 import fyersModel

def get_fyers_model(client_id, secret_key, redirect_uri, auth_code):
    """
    In order to get started with Fyers API we would like you to do the following things first.
    1. Checkout our API docs :   https://myapi.fyers.in/docsv3
    2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/

    Once you have created an APP you can start using the below SDK 
    """
    grant_type = "authorization_code" 
    response_type = "code"  

    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key, 
        redirect_uri=redirect_uri, 
        response_type=response_type, 
        grant_type=grant_type
    )
    # Set the authorization code in the session object
    session.set_token(auth_code)

    # Generate the access token using the authorization code
    response = session.generate_token()
    print("RES - ", response)
    if response['s'] == 'error':
        return response
    print(f"Access token : {response['access_token']}")

    access_token = response['access_token']

    # Initialize the FyersModel instance with your client_id, access_token, and disable async mode
    

    return access_token

def get_refresh_token(client_id, secret_key, redirect_uri, auth_code):
    """
    In order to get started with Fyers API we would like you to do the following things first.
    1. Checkout our API docs :   https://myapi.fyers.in/docsv3
    2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/
    """
    grant_type = "authorization_code"
    response_type = "code"
    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key, 
        redirect_uri=redirect_uri, 
        response_type=response_type, 
        grant_type=grant_type
    )
    session.set_token(auth_code)

    # Generate the access token using the authorization code
    response = session.generate_token()
    print("RES - ", response)
    if response['s'] == 'error':
        return response
    
    return response['refresh_token']
import json, os
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .scanners.streak import get_scanner_data, get_all_scanners
from rest_framework.decorators import action
from .models import AuthCode
from .serializers import AuthCodeSerializer
from brokers.fyers.get_fyers_model import get_fyers_model, get_refresh_token
from brokers.fyers.orders import place_fyers_order
from brokers.fyers.data import get_quotes
from fyers_apiv3 import fyersModel


class HealthCheckView(ViewSet):
    def list(self, request, *args, **kwargs):
        return Response({'status': 'ok'})
class ScannersDataViewset(ViewSet):

    def list(self, request, *args, **kwargs):
        data = get_all_scanners()
        return Response({'data': data})
    
    def create(self, request, *args, **kwargs):
        try:
            if request.body:
                webhook_data = json.loads(request.body)
                print(webhook_data)
                return Response({'status': 'Webhook received successfully'})
            else:
                return Response({'status': 'No Data Found'})
        except Exception as e:
            print("Error in recieviinig data from webhook", e)
    
    @action(detail=False, methods=["GET"])
    def scanner_details(self, request, *args, **kwargs):
        try:
            scanner_id = self.request.query_params.get("scanner_id", None)
            if scanner_id:
                data = get_scanner_data(scanner_slug=scanner_id)
                return Response({'data': data})
                
        except Exception as e:
            print(f"Error in getting scanners details data : {e}")
            raise e
            
    @action(detail=False, methods=["POST"])
    def stock_prices(self, request, *args, **kwargs):
        try:
            app_id = request.data.get("app_id", None)
            auth_code = request.data.get("auth_code", None)
            secret_key = request.data.get("secret_key", None)
            symbols = request.data.get("symbols", None)
            symbols = ",".join([f"{item}-EQ" for item in symbols])
            fyers = fyersModel.FyersModel(client_id=app_id, is_async=False, token=auth_code, log_path=os.getcwd())
            if isinstance(fyers, dict) and fyers['s'] == 'error':
                return Response(fyers, status=status.HTTP_400_BAD_REQUEST)
            response = get_quotes(fyers, symbols)

            return Response({'data': response}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in getting stock prices data : {e}")


class AuthCodeViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        # Customize the list method if needed
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            app_id = request.data.get("app_id", None)
            auth_code = request.data.get("auth_code", None)
            secret_key = request.data.get("secret_key", None)
            redirect_uri = request.data.get("redirect_uri", None)
            access_token = get_fyers_model(app_id, secret_key, redirect_uri, auth_code)
            return Response({'access_token': access_token}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(f"Error in setting refresh token : {e}")
            raise e

    def update(self, request, *args, **kwargs):
        # Customize the update method if needed
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["POST"])
    def access_token(self, request, *args, **kwargs):
        pass
class OrderPlacementViewset(ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({'status': 'ok'})
    
    def create(self, request, *args, **kwargs):
        """
            This method is used to place an order
        """
        app_id = request.data.get("app_id", None)
        auth_code = request.data.get("auth_code", None)
        secret_key = request.data.get("secret_key", None)
        symbol = request.data.get("symbol", None)
        quantity = request.data.get("qty", None)
        price = request.data.get("price", None)
        order_type = request.data.get("order_type", None)
        side = request.data.get("side", None)
        
        # Validate app_id and auth_code
        if not (app_id or auth_code or secret_key or symbol or order_type or side):
            return Response({"error": "app_id, auth_code, secret_key, symbol, side and order_type are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get fyers model
        try:
            fyers = fyersModel.FyersModel(client_id=app_id, is_async=False, token=auth_code, log_path=os.getcwd())
            if isinstance(fyers, dict) and fyers['s'] == 'error':
                return Response(fyers, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error in getting fyers model : {e}")
            raise e
        
        # Place order
        try:
            response = place_fyers_order(
                fyers=fyers,
                symbol=symbol,
                qty=quantity, 
                order_type=order_type, 
                side=side,
                product_type='CNC',
                )
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error in placing order : {e}")
            raise e
    
    def update(self, request, *args, **kwargs):
        # Customize the update method if needed
        return super().update(request, *args, **kwargs)

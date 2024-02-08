import json
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .scanners.streak import get_scanner_data, get_all_scanners
from rest_framework.decorators import action
from .models import AuthCode
from .serializers import AuthCodeSerializer
from brokers.fyers.get_fyers_model import get_fyers_model
from brokers.fyers.orders import place_fyers_order


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

class AuthCodeViewSet(ModelViewSet):
    queryset = AuthCode.objects.all()
    serializer_class = AuthCodeSerializer

    def list(self, request, *args, **kwargs):
        # Customize the list method if needed
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        # Customize the update method if needed
        return super().update(request, *args, **kwargs)

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
        quantity = request.data.get("quantity", None)
        price = request.data.get("price", None)
        order_type = request.data.get("order_type", None)
        
        # Validate app_id and auth_code
        if not app_id or not auth_code or not secret_key or symbol or order_type:
            return Response({"error": "app_id, auth_code, secret_key, symbol and order_type is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get fyers model
        try:
            fyers_model = get_fyers_model(app_id, secret_key, 'http://192.168.1.4:5173/', auth_code)
        except Exception as e:
            print(f"Error in getting fyers model : {e}")
            raise e
        
        # Place order
        try:
            response = place_fyers_order(
                fyers=fyers_model,
                symbol=symbol,
                qty=quantity, 
                order_type=order_type, 
                side=1,
                product_type='CNC',
                )
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error in placing order : {e}")
            raise e
    
    def update(self, request, *args, **kwargs):
        # Customize the update method if needed
        return super().update(request, *args, **kwargs)

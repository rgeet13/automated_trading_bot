import json
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .scanners.streak import get_scanner_data, get_all_scanners
from rest_framework.decorators import action

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
     
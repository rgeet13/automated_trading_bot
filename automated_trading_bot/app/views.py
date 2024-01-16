import json
from rest_framework.views import APIView
from rest_framework.response import Response

class WebhookDataView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, DRF!'})
    
    def post(self, request, *args, **kwargs):
        try:
            print("REQ BODY -- ",request.body)
            if request.body:
                webhook_data = json.loads(request.body)
                print(webhook_data)
                return Response({'status': 'Webhook received successfully'})
            else:
                return Response({'status': 'No Data Found'})
        except Exception as e:
            print("Error in recieviinig data from webhook", e)
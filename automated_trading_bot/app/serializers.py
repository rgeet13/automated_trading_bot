from rest_framework import serializers
from .models import AuthCode

class AuthCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthCode
        fields = ['id', 'app_id', 'auth_code', 'updated_at', 'broker']

from rest_framework import serializers
from django.contrib.auth.models import User

class AdminLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    username  = serializers.CharField()
    password = serializers.CharField()
    
    
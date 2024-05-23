from rest_framework import serializers
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    username  = serializers.CharField()
    password = serializers.CharField()
    
    
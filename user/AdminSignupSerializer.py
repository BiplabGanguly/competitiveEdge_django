from rest_framework import serializers
from django.contrib.auth.models import User
from user import models
import re
from django.db import transaction

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Profile
        fields = [
            'user_title', 
            'user_mobile_no', 
            'user_date_of_birth', 
            'user_gender', 
            'user_identity', 
            'identity_number'
        ]

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Address
        fields = [
            'user_address', 
            'user_city', 
            'user_pin_code', 
            'user_country'
        ]

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Data
        fields = ['profile', 'permission']

class UserSignupSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    user_address = UserAddressSerializer()
    user_data = UserDataSerializer()
    
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'username', 
            'password', 
            'user_profile', 
            'user_address', 
            'user_data'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_first_name(self, value):
        if not re.match("^[A-Za-z]*$", value):
            raise serializers.ValidationError("First name must contain only letters.")
        return value

    def validate_last_name(self, value):
        if not re.match("^[A-Za-z]*$", value):
            raise serializers.ValidationError("Last name must contain only letters.")
        return value

    def validate_email(self, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", value):
            raise serializers.ValidationError("Email must be a valid Gmail address.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*()_+=-]", value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value

    def validate_user_profile(self, value):
        if not re.match("^[0-9]{10}$", value['user_mobile_no']):
            raise serializers.ValidationError("Mobile number must be exactly 10 digits.")
        return value

    def validate_user_data(self, value):
        if value['profile'] not in ["admin", "student", "faculty"]:
            raise serializers.ValidationError("Profile must be 'admin', 'student', or 'faculty'.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        user_profile_data = validated_data.pop('user_profile')
        user_address_data = validated_data.pop('user_address')
        user_data_data = validated_data.pop('user_data')

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create related instances
        models.User_Profile.objects.create(user=user, **user_profile_data)
        models.User_Address.objects.create(user=user, **user_address_data)
        models.User_Data.objects.create(user=user, **user_data_data)

        return user

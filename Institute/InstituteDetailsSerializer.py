from rest_framework import serializers
from django.contrib.auth.models import User
from Institute.models import InstituteDetails


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteDetails
        fields  = '__all__'
        
    def create(self, validated_data):
        institute_details = InstituteDetails.objects.create(**validated_data)
        return institute_details
    
class InstituteBranchSerializer(serializers.Serializer):
    branch_name = serializers.CharField()
    branch_description =serializers.CharField()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.EmailField(allow_blank=True)

class UserBranchSerializer(serializers.Serializer):
    user = UserSerializer()
    user_branch = InstituteBranchSerializer()
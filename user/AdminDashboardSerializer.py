from rest_framework import serializers


class InstituteBranchSerializer(serializers.Serializer):
    branch_name = serializers.CharField(max_length=100)
    
    

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.EmailField(allow_blank=True)
    


    
    
class UserBranch(serializers.Serializer):
    user = UserSerializer()
    user_branch = InstituteBranchSerializer()
    
    def to_representation(self, instance):
        # Override to_representation to include only one user's details
        user_data = super().to_representation(instance)
        user_data.pop('user')  # Remove 'profile' from the serialized data if not needed
        return user_data
    

    
    
class UserDataSerializer(serializers.Serializer):
    user = UserSerializer()  
    profile = serializers.CharField(max_length=50)
    
    

    
    

     
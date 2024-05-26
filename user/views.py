from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user import AdminSignupSerializer,AdminLoginSerializer,AdminDashboardSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . import models


class AdminRegistration(APIView):

    def post(self, req):
        user_serializer = AdminSignupSerializer.UserSignupSerializer(data=req.data)
        if user_serializer.is_valid():
            user_serializer.save()
            user = User.objects.get(username=user_serializer.validated_data['username'])
            token_obj, _ = Token.objects.get_or_create(user=user)
            response_data = user_serializer.data
            response_data['token'] = token_obj.key
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AdminLoginView(APIView):

    def post(self, req):
        admin_login = AdminLoginSerializer.UserLoginSerializer(data=req.data)
        print("called admin login")
        if admin_login.is_valid():
            print(admin_login.validated_data['username'],admin_login.validated_data['password'],admin_login.validated_data['email'])
            user = authenticate(
                username=admin_login.validated_data['username'],
                password=admin_login.validated_data['password']
            )
            if user is not None:
                if user.email == admin_login.validated_data['email']:
                    try:
                        user_data = models.User_Data.objects.get(user=user)
                    except models.User_Data.DoesNotExist:
                        return Response({"detail": "User data not found"}, status=status.HTTP_404_NOT_FOUND)

                    token_obj, _ = Token.objects.get_or_create(user=user)
                    login(req, user)
                    
                    response_data = {
                        "token": token_obj.key,
                        "admin_id": user.id,
                        "admin_username": user.username,
                        "admin_permission": user_data.permission,
                        "admin_profile" : user_data.profile
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"detail": "Email does not match"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(admin_login.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DataCountAdminDashboard(APIView):
    def get(self,req):
            total_faculty = models.User_Data.objects.filter(profile = 'faculty').count()
            responce_data = {'total_faculty':total_faculty}
            return Response(responce_data,status=status.HTTP_201_CREATED)
        
        

class GetAllUserData(APIView):
    def get(self, req):
        faculty_accepted_users = models.User_Data.objects.filter(profile='faculty', permission='accept')
        faculty_branch = models.UserBranch.objects.filter(user_profile = 'faculty',user_permission = 'accept')
        # serializers
        faculty_data = AdminDashboardSerializer.UserDataSerializer(faculty_accepted_users, many = True)
        faculty_branch_data = AdminDashboardSerializer.UserBranch(faculty_branch,many = True)
        # dict
        responce_data = {'faculty_details':faculty_data.data}
        responce_data['faculty_branch'] = faculty_branch_data.data
        return Response(responce_data,status=status.HTTP_201_CREATED)
        
        
# class GetUserBranch(APIView):
#     def get(self,req):
        
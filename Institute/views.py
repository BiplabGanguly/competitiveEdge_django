from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Institute.InstituteDetailsSerializer import InstituteSerializer,UserBranchSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from user.models import UserBranch
# Create your views here.


class InstituteDetails(APIView):
    
    def post(self, req):
        serializer = InstituteSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class GetallBranchCount(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,req):
        get_all_branch_count = models.InstituteBranch.objects.all().count()
        responce_data = {'get_all_branch_count':get_all_branch_count}
        return Response(responce_data,status=status.HTTP_201_CREATED)
    
class GetFacultyBrancheDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, req, uid):
        all_branches = UserBranch.objects.filter(user_id = uid, user_permission = "accept", user_profile = "faculty")
        branches = UserBranchSerializer(all_branches,many = True)
        responce_data = {'all_branches':branches.data}
        return Response(responce_data,status=status.HTTP_201_CREATED)
        

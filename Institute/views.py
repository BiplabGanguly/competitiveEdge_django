from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Institute.InstituteDetailsSerializer import InstituteSerializer,InstituteBranchSerializer
from . import models
# Create your views here.


class InstituteDetails(APIView):
    
    def post(self, req):
        serializer = InstituteSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class GetallBranchCount(APIView):
    def get(self,req):
        get_all_branch_count = models.InstituteBranch.objects.all().count()
        responce_data = {'get_all_branch_count':get_all_branch_count}
        return Response(responce_data,status=status.HTTP_201_CREATED)
    
class GetallBranches(APIView):
    def get(self, req):
        all_branches = models.InstituteBranch.objects.all()
        branches = InstituteBranchSerializer(all_branches,many = True)
        responce_data = {'all_branches':branches.data}
        return Response(responce_data,status=status.HTTP_201_CREATED)
        

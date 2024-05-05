from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user import serializer


class Admin_ragistration(APIView):

    def post(self,req):
        user_serializer = serializer.ProfileSerializer(data=req.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
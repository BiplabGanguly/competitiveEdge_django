from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .ExamSerializer import ExamViewSerializer,QuestionBoxSerializer
from .models import ExamModel, QuestionBoxModel
from user.models import UserBranch
from Institute.models import InstituteBranch
from datetime import datetime
import pytz
# Create your views here..

def get_current_ist_time():
    utc_now = datetime.utcnow().replace(tzinfo=pytz.UTC)
    ist = pytz.timezone('Asia/Kolkata')
    ist_now = utc_now.astimezone(ist)
    current_date = ist_now.date()
    current_time = ist_now.time()
    return current_date, current_time

class ExamView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request,uid):
        exam_data = ExamViewSerializer(data=request.data)
        if exam_data.is_valid():
            exam_data.save()
            # print(exam_instance.exam_passkey)  
            # print(exam_instance.id)
            return Response({"success":"exam created successfully"}, status=status.HTTP_201_CREATED)
        return Response(exam_data.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, uid):
        user_branch_data = UserBranch.objects.filter(user_id=uid).values_list('user_branch', flat=True)
        branch_data = InstituteBranch.objects.filter(id__in=user_branch_data).values_list('branch_name', flat=True)
        exam_data = ExamModel.objects.filter(is_completed=False, is_deleted=False, exam_branch__in=branch_data)
        exam_serializer = ExamViewSerializer(exam_data, many=True)
        return Response(exam_serializer.data)
    

class CompletedExamView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, uid):
        incomplete_exams = ExamModel.objects.filter(is_completed=False, is_deleted=False)
        current_date, current_time = get_current_ist_time()
        
        for exam in incomplete_exams:
            if ((current_date == exam.exam_date and current_time > exam.exam_end_time) or (current_date > exam.exam_date)):
                exam.is_completed = True
                exam.save()

        user_branch_data = UserBranch.objects.filter(user_id=uid).values_list('user_branch', flat=True)
        branch_data = InstituteBranch.objects.filter(id__in=user_branch_data).values_list('branch_name', flat=True)
        exam_data = ExamModel.objects.filter(is_completed=True, is_deleted=False, exam_branch__in=branch_data)
        exam_serializer = ExamViewSerializer(exam_data, many=True)
        return Response(exam_serializer.data)
    

class QuestionBoxView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, eid):
        serializer = QuestionBoxSerializer(data=request.data, context={'exam_id': eid, 'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, eid):
        questions = QuestionBoxModel.objects.filter(exam_id=eid)
        serializer = QuestionBoxSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

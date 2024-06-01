from rest_framework import serializers
from .models import ExamModel,QuestionBoxModel
from django.contrib.auth.models import User

class ExamViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    exam_name = serializers.CharField()
    exam_desc = serializers.CharField()
    exam_branch = serializers.CharField()
    exam_passkey = serializers.CharField(required=False)
    exam_date = serializers.DateField()
    exam_start_time = serializers.TimeField()
    exam_end_time = serializers.TimeField()
    is_completed = serializers.BooleanField(required=False)
    is_deleted = serializers.BooleanField(required=False)


    def create(self, validated_data):
        exam_data = ExamModel.objects.create(
            exam_name = validated_data['exam_name'], 
            exam_desc = validated_data['exam_desc'],
            exam_branch = validated_data['exam_branch'],
            exam_date = validated_data['exam_date'],
            exam_start_time = validated_data['exam_start_time'],
            exam_end_time = validated_data['exam_end_time'],
            )
        return exam_data
    

class QuestionBoxSerializer(serializers.Serializer):
    user = serializers.CharField(required = False)  
    exam_id  = serializers.CharField() 
    question = serializers.CharField()
    answer1 = serializers.CharField()
    answer2 = serializers.CharField()
    answer3 = serializers.CharField(required=False)
    answer4 = serializers.CharField(required=False)
    currectanswer = serializers.CharField()

    def create(self, validated_data):
        exam_id = validated_data.pop('exam_id')
        exam_data = ExamModel.objects.get(id = exam_id)
        question_box = QuestionBoxModel.objects.create(
            user=self.context['request'].user,
            exam_id=exam_data,
            **validated_data
        )
        return question_box
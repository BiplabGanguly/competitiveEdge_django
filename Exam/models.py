from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ExamModel(models.Model):
    exam_name = models.CharField(max_length=255,unique=True)
    exam_desc = models.TextField()
    exam_branch = models.CharField(max_length=255)
    exam_passkey = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    exam_date = models.DateField()
    exam_start_time = models.TimeField()
    exam_end_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.exam_name
    

class QuestionBoxModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_id  = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    question = models.TextField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255,blank=True)
    answer4 = models.CharField(max_length=255,blank=True)
    currectanswer = models.CharField(max_length=255)

    def __str__(self):
        return self.exam_id.exam_name
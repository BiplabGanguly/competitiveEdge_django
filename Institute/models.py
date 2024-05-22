from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InstituteDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255)
    institute_description = models.TextField()
    institute_headline = models.CharField(max_length=255)
    institute_courses = models.CharField(max_length=255)
    institute_special_recog = models.CharField(max_length=255)
    institute_ref_no = models.CharField(max_length=255) 
     
    def __str__(self):
        return self.institute_name
    
    
class InstituteBranch(models.Model):
    branch_name = models.CharField(max_length=255)
    branch_description = models.TextField()
    
    def __str__(self):
        return self.branch_name




# class ExamdataModel(models.Model):
#     branch_id  = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE)
#     exam_name = models.CharField(max_length=255)
#     exam_desc = models.TextField()
#     exam_date = models.DateField()
#     exam_start_time = models.TimeField()
#     exam_end_time = models.TimeField()



# class QuestionBoxModel(models.Model):
#     exam_id = models.ForeignKey(ExamdataModel, on_delete=models.CASCADE)
#     question = models.TextField()
#     answer1 = models.CharField(max_length=255)
#     answer2 = models.CharField(max_length=255)
#     answer3 = models.CharField(max_length=255)
#     answer4 = models.CharField(max_length=255)
#     actualanswer = models.CharField(max_length=255)
    
    
    
# class ScoreBoxModel(models.Model):
#     exam_id = models.ForeignKey(ExamdataModel, on_delete=models.CASCADE)
#     student_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     exam_score = models.CharField(max_length=255)

    
from django.db import models
from django.contrib.auth.models import User
from Institute.models import InstituteBranch

# Create your models here.

profile_choice = [
    ('faculty','faculty'),
    ('student','student')
]

permissions = [
    ('pending','pending'),
    ('accept','accept'),
    ('reject','reject')
]



class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_title = models.CharField(blank=True,max_length=50 )
    user_mobile_no = models.CharField(blank=True, max_length=50)
    user_date_of_birth = models.CharField(blank=True, max_length=50)
    user_gender = models.CharField(blank=True, max_length=50)
    user_identity = models.CharField(max_length=255, blank=True)
    identity_number = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    
    
    
    
    
class User_Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_address = models.TextField()
    user_city = models.CharField(max_length=255, blank=True)
    user_pin_code = models.CharField(max_length=255, blank=True)
    user_country = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
    
    
    
class User_Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.CharField(choices=profile_choice, max_length=50)
    permission = models.CharField(choices=permissions, max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
    
class UserBranch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE)
    user_profile = models.CharField(choices=profile_choice, max_length=50)
    user_permission = models.CharField(choices=permissions, max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username



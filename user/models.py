from django.db import models
from django.contrib.auth.models import User

# Create your models here.

profile_choice = [
    ('admin','admin'),
    ('faculty','faculty'),
    ('student','student')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile = models.CharField(choices=profile_choice,max_length = 50)
    user_title = models.CharField(blank=True,max_length=50 )
    user_mobile_no = models.CharField(blank=True, max_length=50)
    user_date_of_birth = models.CharField(blank=True, max_length=50)
    user_gender = models.CharField(blank=True, max_length=50)
    user_address = models.TextField()
    user_city = models.CharField(max_length=255, blank=True)
    user_pin_code = models.CharField(max_length=255, blank=True)
    user_country = models.CharField(max_length=255, blank=True)
    user_identity = models.CharField(max_length=255, blank=True)
    identity_image = models.FileField(upload_to='identity_images/', blank=True)
    admin_institute = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username





from django.contrib import admin
from user import models
# Register your models here.
admin.site.register(models.User_Profile)
admin.site.register(models.User_Address)
admin.site.register(models.User_Data)
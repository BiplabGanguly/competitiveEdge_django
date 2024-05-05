from django.urls import path
from user import views

urlpatterns = [
    path('admin-ragistration/',views.Admin_ragistration.as_view())
]
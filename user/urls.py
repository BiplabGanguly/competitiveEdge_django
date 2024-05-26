from django.urls import path
from user import views

urlpatterns = [
    path('admin-signup/',views.AdminRegistration.as_view()),
    path('admin-signin/',views.AdminLoginView.as_view()),
    path('total-faculty/',views.DataCountAdminDashboard.as_view()),
    path('faculty-details/', views.GetAllUserData.as_view()),
]
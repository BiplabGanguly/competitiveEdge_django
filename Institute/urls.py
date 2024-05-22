from django.urls import path
from Institute import views

urlpatterns = [
    path('register/',views.InstituteDetails.as_view()),
    path('branch-count/',views.GetallBranchCount.as_view()),
    path('branch-details/',views.GetallBranches.as_view()),
]
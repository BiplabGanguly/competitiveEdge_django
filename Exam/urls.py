from django.urls import path
from . import views

urlpatterns = [
    path('exam-data/<uid>/',views.ExamView.as_view()),
    path('complete-exam/<uid>/',views.CompletedExamView.as_view()),
    path('questionbox/<eid>/',views.QuestionBoxView.as_view()),
]
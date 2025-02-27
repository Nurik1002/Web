# teachers/urls.py
from django.urls import path
from .views import TeacherCreateView, TeacherSuccessView

urlpatterns = [
    path('', TeacherCreateView.as_view(), name='teacher_create'),
    path('success/', TeacherSuccessView.as_view(), name='teacher_success'),
]
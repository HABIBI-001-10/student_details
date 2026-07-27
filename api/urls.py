from django.urls import path
from . import views

urlpatterns = [
    path('students1/', views.studentsView),
    path('students2/', views.students),
]
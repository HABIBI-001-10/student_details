from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('api/students/', views.student_list, name='student_list_api')
]
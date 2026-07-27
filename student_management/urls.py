from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('view/', views.view_student, name='view_student'),
    path('view/email/<str:email>/', views.view_student, name='view_student_by_email'),
    path('update/', views.update_student, name='update_student'),
    path('delete/', views.delete_student, name='delete_student'),
]
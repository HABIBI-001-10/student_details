from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def studentsView(request):
    students={
        'id': 1,
        'name': 'John Doe',
        'class': '10th Grade',
    }
    return JsonResponse(students)

def students(request):
    return JsonResponse({'message': 'Hello, World!'})
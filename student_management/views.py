from django.shortcuts import get_object_or_404, redirect, render ,get_list_or_404
from django.http import HttpResponse
from . models import Student

# Create your views here.
def add_student(request):
    if request.method == 'POST':
        # Process the form data and save the student
        name = request.POST.get('name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        department = request.POST.get('department')

        Student.objects.create(
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            department=department
        )
        
        return redirect('view_student')  # Redirect to the view_student page after adding
    return render(request, 'add_student.html')

def view_student(request, email=None):
    if request.method == 'POST':
        student_email = request.POST.get('email')
        return redirect('view_student_by_email', email=student_email)
    if email:
        student =get_object_or_404(Student, email=email )
        return render(request, 'view_student.html', {'student': student})
    students = Student.objects.all()
    return render(request, 'view_student.html', {'students': students})

def update_student(request):
    if request.method == 'POST':
        # Process the form data and update the student
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        department = request.POST.get('department')

        student = Student.objects.get(id=student_id)
        student.name = name
        student.email = email
        student.date_of_birth = date_of_birth
        student.department = department
        student.save()

        return redirect('view_student')  # Redirect to the view_student page after updating
    return render(request, 'update_student.html')

def delete_student(request):
    return render(request, 'delete_student.html')


from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib import messages
from .forms import StudentForm
from .models import Student


# Create your views here.
def home(request):
    return render(request, "home.html")


def add_student(request):

    if request.method == "POST":
        # Process the form data and save the student
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect(
                "view_student"
            )  # Redirect to the view_student page after adding
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})


def view_student(request, email=None):

    if request.method == "POST":
        student_email = request.POST.get("email")
        return redirect("view_student_by_email", email=student_email)
    if email:
        student = get_object_or_404(Student, email=email)
        return render(request, "view_student.html", {"student": student})

    students = Student.objects.all()

    return render(request, "view_student.html", {"students": students})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        # Process the form data and update the student
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            messages.success(request, "Student updated successfully.")

            return redirect(
                "view_student_by_email", email=student.email
            )  # Redirect to the view_student page after updating
    else:
        form = StudentForm(instance=student)
    return render(request, "update_student.html", {"form": form, "student": student})


def delete_student(request, id):

    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])  # Only allow POST requests for deletion
     # Redirect to the view_student page after deleting
    student = get_object_or_404(Student, id=id)

   
    student.delete()

    messages.success(request, "Student deleted successfully.")

    return redirect("view_student")

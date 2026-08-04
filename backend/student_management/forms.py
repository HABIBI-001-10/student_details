from django import forms
from .models import Student
from django.utils import timezone


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "date_of_birth", "department"]

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email").lower().strip()

        existing_student = Student.objects.filter(email=email).exclude(pk=self.instance.pk).first()

        if existing_student:
            raise forms.ValidationError("This email is already in use.")

        return email        
               
        

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")
        if date_of_birth and date_of_birth > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return date_of_birth

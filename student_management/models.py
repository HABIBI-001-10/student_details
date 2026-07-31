from django.db import models

# Create your models here.
class Student(models.Model):
    class Department(models.TextChoices):
        COMPUTER_SCIENCE = "Computer Science","CS"
        MATHEMATICS = "Mathematics","MATH"
        PHYSICS = "Physics","PHY"
        CHEMISTRY = "Chemistry","CHE"
        BIOLOGY = "Biology","BIO"
        ENGINEERING = "Engineering","ENG"
        BUSINESS = "Business","BUS"
        LITERATURE = "Literature","LIT"
        HISTORY = "History","HIST"
        ART = "Art","ART"

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50, choices=Department.choices)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_department_display()}"
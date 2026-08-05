from django.db import models

# Create your models here.
class Student(models.Model):
       
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
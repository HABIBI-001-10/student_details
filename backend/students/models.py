from django.db import models

# Create your models here.
class Student(models.Model):

    class GenderChoices(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    class DepartmentChoices(models.TextChoices):
        CSE = 'CSE', 'Computer Science and Engineering'
        ECE = 'ECE', 'Electronics and Communication Engineering'
        MECH = 'MECH', 'Mechanical Engineering'
        CIVIL = 'CIVIL', 'Civil Engineering'
        IT = 'IT', 'Information Technology'

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    student_id = models.CharField(max_length=10, unique=True)   
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50, choices=DepartmentChoices.choices)
    semester = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enrollment_date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
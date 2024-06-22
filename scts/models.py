from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    classroom = models.CharField(max_length=50)

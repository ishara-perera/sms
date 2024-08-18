import uuid
from datetime import date

from django.db import models


# Create your models here.


class Student(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    classroom = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if self.dob:
            today = date.today()
            self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        super().save(*args, **kwargs)

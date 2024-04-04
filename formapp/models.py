from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "students"

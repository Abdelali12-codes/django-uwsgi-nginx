from django.db import models

# Create your models here.
class Web(models.Model):
    firstname = models.CharField(max_length=200)
    lastbname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    class Meta: 
        db_table="webapp"
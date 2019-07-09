from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    county = models.CharField(max_length=128)
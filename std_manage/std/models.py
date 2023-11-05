from django.db import models

# Create your models here.
# DIV_CHOICES = (
#     ('ce','CE'),
#     ('cse', 'CSE'),
#     ('extc','EXTC'),
# )

class Student(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    division = models.CharField(max_length=10, default='CE')

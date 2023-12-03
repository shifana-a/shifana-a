from django.db import models

# Create your models here.




class Department(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

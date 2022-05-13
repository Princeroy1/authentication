from django.db import models

# Create your models here.
class student_signup(models.Model):
    User_Name=models.CharField(max_length=60)
    Full_Name=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=100)
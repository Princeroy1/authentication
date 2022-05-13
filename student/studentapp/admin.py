from django.contrib import admin
from .models import student_signup
# Register your models here.
@admin.register(student_signup)
class student_signup(admin.ModelAdmin):
    list_display= ['User_Name']
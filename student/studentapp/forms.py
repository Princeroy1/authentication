import imp
from .models import student_signup
from django import forms
from django.contrib.auth.forms import UserCreationForm

class signup(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=student_signup
        fields='__all__'
    
class loginform(UserCreationForm):
    name=forms.CharField(max_length=123)  
    username = forms.CharField(label='User Name', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput) 
    password2 = forms.CharField(label=' Confirm password', widget=forms.PasswordInput) 
    fields=[name,username]
    
  
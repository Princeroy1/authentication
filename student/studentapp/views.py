from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import signup,loginform
from django.contrib.auth import login,authenticate
from.models import student_signup
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib import messages
def Registration(request):
 if request.method=='POST':
  fm=loginform(request.POST)
  if fm.is_valid():
   messages.success(request,'Your Account has been Created')
   fm.save()
   fm=loginform()
 else:
  fm=loginform()
 return render(request,'signup.html',{'forms':fm})

def Userlogin(request):
    if request.method=='POST':
     fm = AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
        usern=fm.cleaned_data['username']
        passw=fm.cleaned_data['password']
        user=authenticate(username=usern,password=passw)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request, 'login.html',{'forms':fm})   
    #    form = userlogin(request.POST)
    #    if form.is_valid():
    #     ur = form.cleaned_data['User_Name']
    #     pd = form.cleaned_data['Password']
    #     dbuser = student_signup.objects.filter(User_Name=ur, Password=pd)
    #     if not dbuser:
    #      return HttpResponse('Login failed')
    #     else:
    #      return HttpResponseRedirect('/profile/')
    #  else:
      
  
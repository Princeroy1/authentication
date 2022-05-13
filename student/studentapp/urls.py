from django.urls import path
from studentapp import views
urlpatterns = [
   path('signup/',views.Registration,name='signup'),
   path('login/',views.Userlogin,name='login'),
]

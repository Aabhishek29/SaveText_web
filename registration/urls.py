from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path(r'getUserLogin',views.getUserLogin,name='getUserLogin'),
    path(r'RegistrationForm',views.RegistrationForm,name='RegistrationForm')
]
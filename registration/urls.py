from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('getUserLogin',views.getUserLogin,name='getUserLogin'),
    path('RegistrationForm',views.RegistrationForm,name='RegistrationForm')
]
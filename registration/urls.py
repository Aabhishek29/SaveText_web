from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path(r'getUserLogin',views.getUserLogin,name='getUserLogin'),
    path(r'registerUser',views.registerUser,name='registerUser'),
    path(r'forgetIdPass',views.changeIdPassword,name='changeIdPassword'),
    path(r'getUserInfoRegister',views.getUserInfoRegister,name='getUserInfoRegister'),
]
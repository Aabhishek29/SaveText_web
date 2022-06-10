from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path(r'getUserLogin',views.getUserLogin,name='getUserLogin'),
    path(r'registerUser',views.registerUser,name='registerUser'),
    path(r'forgetIdPass',views.changeIdPassword,name='changeIdPassword'),
    path(r'getUserInfoRegister',views.getUserInfoRegister,name='getUserInfoRegister'),
    path(r"send_otp",views.send_otp,name="send otp"),
    path(r'confirm_otp',views.renderOtpPage,name='renderOtpPage'),
    path(r'verifyOTP',views.verifyOTP,name='verifyOTP')
]
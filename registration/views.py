import re
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from .models import UserRegistration
from .form import RegistrationForm
import uuid
from django.contrib import messages
from django.core.mail import send_mail
import math, random

validEmailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

validNameRegex = re.compile(r'^([a-z]+)*( [a-z]+)*$',re.IGNORECASE)

def home(request):
    return render(request,'home.html')


def authenticateUser(userId , password):
    auth = UserRegistration.objects.raw(f'''
            SELECT name FROM UserRegistration
            WHERE username = {userId} AND password = {password}
        ''')
    print(auth)
    return 0


def getUserLogin(request):
    if request.method == 'POST':
        print('Login Method : getting username and password ')
        username = request.POST['username']
        password = request.POST['password']
        
        password = request.POST['password']
        print(f'username : {username} \n password : {password}')
        
        if(not(re.fullmatch(validEmailRegex, username))):
            messages.info(request,"Please enter valid email address")
            return HttpResponseRedirect('/')

        if(authenticateUser(username , password)):
            return HttpResponseRedirect('/')
        sessionId = genrateUUId()
        print(f'session id : {sessionId}')
    return render(request,'textUtils.html')

def changeIdPassword(request):
    return render(request,'forgetIdPass.html')

def getUserInfoRegister(request):
    if request.method == 'POST':

        db_obj = UserRegistration()
        db_obj.name = request.POST['name']
        if(not(re.fullmatch(validNameRegex, db_obj.name))):
            messages.info(request,"Please enter valid Name")
            return HttpResponseRedirect('/registerUser')
        db_obj.email = request.POST['email']
        if(not(re.fullmatch(validEmailRegex, db_obj.email))):
            messages.info(request,"Please enter valid email address")
            return HttpResponseRedirect('/registerUser')
        db_obj.password = request.POST['password']
        if(len(db_obj.password)<8):
            messages.info(request,"Password should be of length 8 characteres")
            return HttpResponseRedirect('/registerUser')
        db_obj.confirm_password = request.POST['confirm_password']
        if(db_obj.password != db_obj.confirm_password):
            messages.info(request,"Password doesn't match")
            return HttpResponseRedirect('/registerUser')
        db_obj.hint_question = request.POST['hint_question']
        db_obj.hint_answer = request.POST['hint_answer']

        db_obj.userId = genrateUUId()
        try:
            res = send_otp(request,db_obj.email)
            if(res):
                print('data saved Sucessfully...')
                return render(request,'checkOtp.html')
            # db_obj.save()
        except Exception as e:
            messages.info(request,"Email Id already")
            messages.info(request,"Email Id already exist Please goto Forget Password to retrive your Account")
            print(e)
            return HttpResponseRedirect('/registerUser')
        return render(request, 'Home.html')
    return render(request,'/')


def genrateUUId():
    return uuid.uuid4().hex[:15]

def registerUser(request):
    # form = RegistrationForm()
    return render(request,'Registration.html')



def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP


def send_otp(request,emailId):
    try:
        email=request.GET.get("email")
    except Exception as e:
        print(e)
    email = emailId
    print(email)
    o=generateOTP()
    print(o)
    htmlgen = f'<p>Your OTP is <strong>{o}</strong></p>'
    a = send_mail('OTP request',o,'startabhishek29@gmail.com',[email], fail_silently=False, html_message=htmlgen)
    if(a==0):
        print('not send')
        return False
    else:   
        print('sent succesfully')
    return True

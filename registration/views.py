import re
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from .models import UserRegistration
import uuid
from django.contrib import messages
from django.core.mail import send_mail
import math, random

validEmailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

validNameRegex = re.compile(r'^([a-z]+)*( [a-z]+)*$',re.IGNORECASE)

otp_val = ""

db_obj = UserRegistration()

# flag variable is used to confirm_otp
# if flag = 0 used to save new registration data in database
# if flag = 1 used to update password
flag = 1  

def home(request):
    try:
        username = request.COOKIES['name']
        password = request.COOKIES['password']
        print(username+"    "+password)
        if(username!="" and password!=""):
            print("Cookie found")
            print(username+"    "+password)
            if(authenticateUser(username,password)):
                return HttpResponseRedirect('/getUserLogin')
    except Exception as e:
        print("No Cookie Found : ",e)
    return render(request,'home.html')


def authenticateUser(userId , pswd):
    try:
        auth = UserRegistration.objects.get(email=userId)
        if(auth.password == pswd):
            return True
    except Exception as e:
        print("Exception raise on line number 29:",e)
    return False


def getUserLogout(request):
    response = HttpResponseRedirect('/')
    try:
        response.delete_cookie('name')
        response.delete_cookie('password')
    except Exception as e:
        print("Exception in getUserLogout : ",e)
    return response


def getUserLogin(request):
    response = render(request,'textUtils.html')
    if request.method == 'POST':
        print('Login Method : getting username and password ')
        username = request.POST['username']
        password = request.POST['password']
        
        password = request.POST['password']
        print(f'username : {username} \n password : {password}')
        
        if(not(re.fullmatch(validEmailRegex, username))):
            messages.info(request,"Please enter valid email address")
            return HttpResponseRedirect('/')

        if(not authenticateUser(username , password)):
            return HttpResponseRedirect('/')
        response.set_cookie('name',username)
        response.set_cookie('password',password)
        sessionId = genrateUUId()
        print(f'session id : {sessionId}')
    return response

def changeIdPassword(request):
    return render(request,'forgetIdPass.html')

def getUserInfoRegister(request):
    if request.method == 'POST':
        global db_obj
        db_obj.name = request.POST['username']
        if(not(re.fullmatch(validNameRegex, db_obj.name))):
            messages.info(request,"Please enter valid Name")
            return HttpResponseRedirect('/registerUser')
        db_obj.email = request.POST['email']
        if(not(re.fullmatch(validEmailRegex, db_obj.email))):
            messages.info(request,"Please enter valid email address")
            return HttpResponseRedirect('/registerUser')
        db_obj.password = request.POST['pswd']
        if(len(db_obj.password)<8):
            messages.info(request,"Password should be of length 8 characteres")
            return HttpResponseRedirect('/registerUser')
        db_obj.confirm_password = request.POST['conf_pswd']
        if(db_obj.password != db_obj.confirm_password):
            messages.info(request,"Password doesn't match")
            return HttpResponseRedirect('/registerUser')
        db_obj.hint_question = request.POST['hint_question']
        db_obj.hint_answer = request.POST['hint_answer']

        db_obj.userId = genrateUUId()
        try:
            res = send_otp(request,db_obj.email)
            if(res):
                global flag
                flag = 0
                print('data saved Sucessfully...')
                return render(request,'checkOtp.html')
           
        except Exception as e:
            messages.info(request,"Email Id already")
            messages.info(request,"Email Id already exist Please goto Forget Password to retrive your Account")
            print("Error Message On Line Number 84: ",e)
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
        print("Error Message On Send_otp Line Number 110: ",e)
    email = emailId
    print(email)
    global otp_val
    otp_val=generateOTP()
    print(otp_val)
    htmlgen = f'<p>Your OTP is <strong>{otp_val}</strong></p>'
    a = send_mail('OTP request',otp_val,'starkabhishek29@gmail.com',[email], fail_silently=False, html_message=htmlgen)
    if(a==0):
        print('not send')
        return False
    else:   
        print('sent succesfully')
    return True


def renderOtpPage(request):
    return render(request,'checkOtp.html')


def verifyOTP(request):
    global flag
    if request.method == 'GET':
        print("OTP verifing")
        firstVal = request.GET['input1']
        secondVal = request.GET['input2']
        thirdVal = request.GET['input3']
        fourthVal = request.GET['input4']

        val = firstVal+secondVal+thirdVal+fourthVal

        print(f'OTP genrated is: {otp_val} and OTP user entered is: {val}')
        print(f'OTP genrated is: {type(otp_val)} and OTP user entered is: {type(val)}')
        print(f"flag value for this operation is {flag}")
        if(str(val)==str(otp_val) and flag==0):
            print("OTP varified")
            db_obj.save()
            db_obj.clean()
            flag=1
            return render(request,'home.html')
        else:
            return HttpResponseRedirect('/')

    return HttpResponse("<h1>OTP Not Matched</h1>")


'''
    function need to complete by creating a new web page which contain
    password and confirm password text field and after that password field
    of that person must be update
'''

def forgetIdPassword(request):
    global flag
    if request.method == 'GET':
        email = request.GET['email']
        try:
            res = send_otp(request,email)
            flag = 1
            if(res):
                return HttpResponseRedirect("/confirm_otp")
        except Exception as e:
            print("OTP Not send becouse of : ",e)
    return render(request,'forgetIdPass.html')


def save_users_content(request):
    data = request.POST['text']
    return HttpResponse("data value saved")

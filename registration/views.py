from django.shortcuts import render
from .models import UserRegistration
from .form import RegistrationForm
import uuid
# Create your views here.
def home(request):
    return render(request,'home.html')


def getUserLogin(request):
    if request.method == 'POST':
        print('Login Method : getting username and password ')
        username = request.POST['username']
        password = request.POST['password']
        print(f'username : {username} \npassword : {password}')
        
        auth = UserRegistration.objects.raw(f'''
            SELECT name FROM UserRegistration
            WHERE username = {username} AND password = {password}
        ''')

        print(auth)
    return render(request,'textUtils.html')

def changeIdPassword(request):
    return render(request,'forgetIdPass.html')

def getUserInfoRegister(request):
    if request.method == 'POST':

        db_obj = UserRegistration()
        
        db_obj.name = request.POST['name']
        db_obj.email = request.POST['email']
        db_obj.password = request.POST['password']
        db_obj.confirm_password = request.POST['confirm_password']
        db_obj.hint_question = request.POST['hint_question']
        db_obj.hint_answer = request.POST['hint_answer']
        # db_obj.id = uuid.uuid4().hex[:15].upper()

        db_obj.save()
        print('data saved Sucessfully...')
        return render(request, 'Home.html')
    return render(request,'/')

def registerUser(request):
    form = RegistrationForm()
    return render(request,'Registration.html',{'form':form})
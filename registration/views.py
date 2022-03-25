from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def getUserLogin(request):
    return render(request,'textUtils.html')
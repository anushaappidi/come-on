from django.shortcuts import render 
from django.contrib.auth import authenticate 
from django.shortcuts import  redirect
from django.contrib.auth import login as auth_login
from .models import Student
from django.contrib import messages

def home(request):
    return render(request, 'user/home.html')

def home1(request):
    return render(request, 'user/home1.html')

# Create your views here.


def login(request):
    print("helloooooooooooooooo")
    if request.method == 'POST':
        print(request.body)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            try:
                 user = Student.objects.get(student_name__pk=user.id)
                 return redirect('home')
            except Student.DoesNotExist :
                    user = None
                    return redirect('home1')
        else:
             return render(request, "user/login.html", context={
        'sent': True
    })
            # messages.success(request, 'wrong password or username please check')        
    else:
        # Return an 'invalid login' error message.
         return render(request, 'user/login.html' )

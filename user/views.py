from django.shortcuts import render 
from django.contrib.auth import authenticate 
from django.shortcuts import  redirect
from django.contrib.auth import login as auth_login
from .models import Student
from django.contrib import messages
from django.contrib.auth import logout
from feedback.models import Feedback

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
                 student = Student.objects.get(student_name__pk=user.id)
                 form_filled=Feedback.objects.filter(entry_by__pk=student.id)
                 if form_filled is not  None:
                     return redirect('home')
                 else:
                    return render(request,"user/home.html",context={'filled':True})
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

def logout_view(request):
    logout(request)
    return render(request,'user/logout.html')

   

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def homepage(request):
    return render(request,'homeapp/homepage.html')

def login(request):
    return render(request, 'homeapp/login.html')

# homeapp/views.py


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('student_dashboard')
            elif len(username) == 4:
                return redirect('teacher_dashboard')
            elif len(username) == 6:
                return redirect('admin_dashboard')
        else:
            messages.info(request, 'Invalid creditetials')
            return render(request, 'homeapp/login.html')
    else:
        return render(request, 'homeapp/login.html')



def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username,password1)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'homeapp/signup.html')

def logout_view(request):
    auth.logout(request)
    return redirect('login')

def teacher_dashboard(request):
    return render(request, 'teacherapp/teacher_dashboard.html')

def student_dashboard(request):
    return render(request, 'studentapp/student_dashboard.html')

def admin_dashboard(request):
    return render(request, 'adminapp/admin_dashboard.html')






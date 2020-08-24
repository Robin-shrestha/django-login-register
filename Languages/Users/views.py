from django.shortcuts import render, redirect, HttpResponse
from .forms import  RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='login')
def index(request):
    return render(request, 'home/home.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password incorrect')


    return render(request, 'login/login.html')


def registerPage(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account was created for {username}')
            return redirect('login')

    else:
        form = RegisterForm()

    context = {'form':form}
    return render(request, 'register/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
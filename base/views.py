from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datefinder
from django.contrib import messages
from .models import CustomUser

# Create your views here.


def loginPage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = CustomUser.objects.filter(email=email)
        except:
            user = None
        if user:
            user = CustomUser.objects.filter(
                email=email, password=password).first()
            if not user:
                messages.error(request, 'Username/Password do not match')
                return render(request, 'base/loginPage.html')
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, ('User not found!'))
            return render(request, 'base/loginPage.html')

    return render(request, 'base/loginPage.html')


def registerPage(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        date = list(datefinder.find_dates(request.POST['dob']))[0]
        phone = request.POST['phone']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if user:
            messages.error(request, ("User already exists!"))
        else:
            user = CustomUser.objects.create(
                username=name, password=password, email=email, dob=date, phone=phone)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'base/registerPage.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'base/main.html')

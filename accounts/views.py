from django.shortcuts import render, redirect


def home(request):
    return render(request, 'accounts/home.html')


def signupuser(request):
    return render(request, 'accounts/signupuser.html')


def loginuser(request):
    return render(request, 'accounts/loginuser.html')


def logoutuser(request):
    return redirect('home')
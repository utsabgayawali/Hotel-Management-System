from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request,'accounts/register.html')

def login_view(request):
    return render(request,'accounts/login.html')

def my_bookings(request):
    return render(request,'accounts/my_bookings.html')

def profile_view(request):
    return render(request,'accounts/profile.html')

def forgot_password(request):
    return render(request,'accounts/forgot_password.html')

def reset_password(request):
    return render(request,'accounts/reset_password.html')
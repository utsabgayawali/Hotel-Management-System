from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .form import RegesterForm,LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

# Create your views here.



class RegesterView(SuccessMessageMixin,CreateView):
    form_class = RegesterForm
    template_name ='accounts/register.html'
    success_url = reverse_lazy('login')
    success_message= "Account created successfully. Please login."


class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user =True

    def get_success_url(self):
        return reverse_lazy('profile')























def my_bookings(request):
    return render(request,'accounts/my_bookings.html')

def profile_view(request):
    return render(request,'accounts/profile.html')

def forgot_password(request):
    return render(request,'accounts/forgot_password.html')

def reset_password(request):
    return render(request,'accounts/reset_password.html')
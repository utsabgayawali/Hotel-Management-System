from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class RegesterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-input",
        "placeholder": "Username"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-input",
        "placeholder": "Email",
        "required": True
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-input",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-input",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields =['username','email','password1','password2']

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email






class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "class": "form-input",
        "placeholder": "Email address"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-input",
        "placeholder": "Password"
    }))

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

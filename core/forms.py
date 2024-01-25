from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class LogInForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10)

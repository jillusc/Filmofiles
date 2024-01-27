from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text="(min. 8 characters)"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Sorry - this username already exists")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError(
                "Password must be 8 characters or more")

        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Password must contain an uppercase letter")

        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Password must contain a lowercase letter")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password',
                           "Passwords do not match")

        return cleaned_data


class LogInForm(AuthenticationForm):
    pass


class EditReviewForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)


class EditCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import SignUpForm, LogInForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,
                                            password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'core/sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LogInForm()
    return render(request, 'core/log_in.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LogInForm
from content.forms import ReviewForm, CommentForm
from content.models import Review, Comment


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


@login_required
def my_profile(request):
    user_reviews = Review.objects.filter(author=request.user)
    user_comments = Comment.objects.filter(user_name=request.user)
    return render(request, 'core/my_profile.html', {'reviews': user_reviews,
                                                    'comments': user_comments})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'core/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('my_profile')


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'core/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('my_profile')


@login_required
def delete_account(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect('home')

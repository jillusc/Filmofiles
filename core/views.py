from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LogInForm, EditReviewForm, EditCommentForm
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
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == 'POST':
        form = EditReviewForm(request.POST)
        if form.is_valid():
            review.content = form.cleaned_data['content']
            review.save()
            return redirect('my_profile')
    else:
        form = EditReviewForm(initial={'content': review.content})

    return render(request, 'core/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('my_profile')


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user_name=request.user)

    if request.method == 'POST':
        form = EditCommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('my_profile')
    else:
        form = EditCommentForm(initial={'content': comment.content})

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

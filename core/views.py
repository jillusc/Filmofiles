from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm, LogInForm, EditReviewForm, EditCommentForm
from content.models import Review, Comment


def signup_view(request):
    """This view handles user registration.
    Upon successful registration, the user is automatically logged in and
    redirected to the home page. First, it checks if the user is already logged in
    and in such cases prints a message and redirects to their profile page.
    """
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('my_profile')
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
    """This view handles user login.
    Upon successful login, the user is redirected to the home page.
    """
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
def logout_view(request):
    """This view handles user logout.
    Upon successful logout, the user is redirected to the home page, where
    a success message is displayed.
    """
    messages.success(request, "You have been successfully logged out.")
    logout(request)
    return redirect(reverse_lazy('home'))


@login_required
def my_profile(request):
    """
    This view displays user's profile page, showing their submitted reviews and
    comments.
    """
    user_reviews = Review.objects.filter(author=request.user)
    user_comments = Comment.objects.filter(user_name=request.user)
    return render(request, 'core/my_profile.html', {'reviews': user_reviews,
                                                    'comments': user_comments})


@login_required
def edit_review(request, review_id):
    """
    This view allows the author of a review to edit its content in a new page
    and save the changes. It redirects back to the my_profile page.
    """
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == 'POST':
        form = EditReviewForm(request.POST)
        if form.is_valid():
            review.content = form.cleaned_data['content']
            review.save()
            messages.success(request, 'Review successfully updated')
            return redirect('my_profile')

            return redirect('my_profile')
    else:
        form = EditReviewForm(initial={'content': review.content})

    return render(request, 'core/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    """
    This view allows the author of a review to delete it.
    """
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(
                request, "Your review has been deleted!")
    return redirect('my_profile')



@login_required
def confirm_delete_review(request, review_id):
    """
    This view allows the author of a review to confirm deletion of it.
    """
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'core/confirm_delete_review.html', {'review': review})


@login_required
def edit_comment(request, comment_id):
    """
    This view allows the author of a comment to edit its content in a new page
    and save the changes. It redirects back to the my_profile page.
    """
    comment = get_object_or_404(Comment, id=comment_id, user_name=request.user)

    if request.method == 'POST':
        form = EditCommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.save()
            messages.success(request, 'Comment successfully updated')

            return redirect('my_profile')
    else:
        form = EditCommentForm(initial={'content': comment.content})

    return render(request, 'core/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    """
    This view allows the author of a comment to delete it.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('my_profile')


@login_required
def confirm_delete_comment(request, comment_id):
    """
    This view allows the author of a comment to confirm deletion of it.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    return render(request, 'core/confirm_delete_comment.html',
                  {'comment': comment})
            

@login_required
def delete_account(request):
    """
    This view allows the user to delete their account. It redirects to the
    home page.
    """
    user = request.user
    user.delete()
    logout(request)
    return redirect('home')
